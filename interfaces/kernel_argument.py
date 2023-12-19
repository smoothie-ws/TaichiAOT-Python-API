from ctypes import sizeof, memmove, POINTER, cast
from typing import Any

import numpy as np

from taichiAOT.c_api import *
from ._type_maps import *
from .memory import Memory
from .runtime import Runtime


class KernelArgument:
    def __init__(self, ti_runtime: Runtime, arg: Any):
        self.og = arg
        self.allocated_memory = None
        self.type: TiArgumentType = get_ti_argument_type(self.og)
        self.value: TiArgumentValue = self._to_ti_value(self.og, ti_runtime)

    def _to_ti_value(self, arg, ti_runtime) -> TiArgumentValue:
        type_value_map = {
            TiArgumentType.TI_ARGUMENT_TYPE_I32:
                lambda x: TiArgumentValue(i32=x),

            TiArgumentType.TI_ARGUMENT_TYPE_F32:
                lambda x: TiArgumentValue(f32=x),

            TiArgumentType.TI_ARGUMENT_TYPE_NDARRAY:
                lambda x: TiArgumentValue(ndarray=self._to_ti_ndarray(x, ti_runtime))
        }

        return type_value_map.get(self.type, lambda x: None)(arg)

    def _to_ti_ndarray(self, array: np.ndarray, ti_runtime):
        size = array.size
        memory_allocate_info = TiMemoryAllocateInfo(
            size=size * sizeof(get_ctypes_data_type(array)),
            host_write=TI_TRUE,
            host_read=TI_TRUE,
            export_sharing=TI_FALSE,
            usage=TiMemoryUsageFlags.TI_MEMORY_USAGE_STORAGE_BIT)

        self.allocated_memory = Memory.allocate(ti_runtime, memory_allocate_info)
        mapped_data = self.allocated_memory.map()
        data_array = cast(mapped_data, POINTER(size * get_ctypes_data_type(array)))

        memmove(data_array, array.ctypes.data, size * sizeof(get_ctypes_data_type(array)))
        self.allocated_memory.unmap()

        array_shape = TiNdShape(dim_count=len(array.shape), dims=(c_uint32 * 16)(*list(array.shape)))
        return TiNdArray(
            memory=self.allocated_memory.memory_instance,
            shape=array_shape,
            elem_shape=array_shape,
            elem_type=get_ndarray_ti_data_type(array)
        )

    @property
    def get_ti_argument(self) -> TiArgument:
        return TiArgument(
            type=self.type,
            value=self.value
        )
