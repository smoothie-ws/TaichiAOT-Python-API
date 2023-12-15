from ctypes import sizeof, memmove, POINTER, cast
from typing import Any

from .Memory import memory
from .utils import *


class kernel_argument:
    def __init__(self, runtime: TiRuntime, arg: Any):
        self.og = arg
        self.allocated_memory = None
        self.type: TiArgumentType = self._to_ti_type(arg)
        self.value: TiArgumentValue = self._to_ti_value(arg, runtime)

    def _to_ti_type(self, arg) -> TiArgumentType:
        type_map = {
            int: TiArgumentType.TI_ARGUMENT_TYPE_I32,
            float: TiArgumentType.TI_ARGUMENT_TYPE_F32,
            np.ndarray: TiArgumentType.TI_ARGUMENT_TYPE_NDARRAY
        }

        return type_map.get(type(arg))

    def _to_ti_value(self, arg, ti_runtime) -> TiArgumentValue:
        type_value_map = {
            TiArgumentType.TI_ARGUMENT_TYPE_I32: lambda x: TiArgumentValue(i32=x),
            TiArgumentType.TI_ARGUMENT_TYPE_F32: lambda x: TiArgumentValue(f32=x),
            TiArgumentType.TI_ARGUMENT_TYPE_NDARRAY: lambda x: TiArgumentValue(
                ndarray=self._to_ti_ndarray(x, ti_runtime))
        }

        return type_value_map.get(self.type, lambda x: None)(arg)

    def _to_ti_ndarray(self, array, ti_runtime):
        size = array.size
        memory_allocate_info = TiMemoryAllocateInfo(
            size=size * sizeof(ctypes_datatype(array)),
            host_write=TI_TRUE,
            host_read=TI_TRUE,
            export_sharing=TI_FALSE,
            usage=TiMemoryUsageFlags.TI_MEMORY_USAGE_STORAGE_BIT)

        self.allocated_memory = memory.allocate(ti_runtime, memory_allocate_info)
        mapped_data = self.allocated_memory.map()
        data_array = cast(mapped_data, POINTER(size * ctypes_datatype(array)))

        memmove(data_array, array.ctypes.data, size * sizeof(ctypes_datatype(array)))
        self.allocated_memory.unmap()

        array_shape = TiNdShape(dim_count=len(array.shape), dims=(c_uint32 * 16)(*list(array.shape)))
        return TiNdArray(
            memory=self.allocated_memory.memory_instance,
            shape=array_shape,
            elem_shape=array_shape,
            elem_type=taichi_datatype(array)
        )

    @property
    def get_ti_argument(self) -> TiArgument:
        return TiArgument(
            type=self.type,
            value=self.value
        )
