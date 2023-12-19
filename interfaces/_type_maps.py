from ctypes import (c_int8, c_int16, c_int32, c_int64, c_uint8, c_uint16,
                    c_uint32, c_uint64, c_float, c_double)

from numpy import dtype, ndarray

from taichiAOT import TiArgumentType, TiDataType


class _TiTypeMap:
    kernel_argument = {
        int: TiArgumentType.TI_ARGUMENT_TYPE_I32,
        float: TiArgumentType.TI_ARGUMENT_TYPE_F32,
        ndarray: TiArgumentType.TI_ARGUMENT_TYPE_NDARRAY,
        bytes: TiArgumentType.TI_ARGUMENT_TYPE_TEXTURE,
        str: TiArgumentType.TI_ARGUMENT_TYPE_SCALAR,
        list: TiArgumentType.TI_ARGUMENT_TYPE_TENSOR,
    }

    ndarray_element = {
        dtype('int8'): TiDataType.TI_DATA_TYPE_I8,
        dtype('int16'): TiDataType.TI_DATA_TYPE_I16,
        dtype('int32'): TiDataType.TI_DATA_TYPE_I32,
        dtype('int64'): TiDataType.TI_DATA_TYPE_I64,
        dtype('uint8'): TiDataType.TI_DATA_TYPE_U8,
        dtype('uint16'): TiDataType.TI_DATA_TYPE_U16,
        dtype('uint32'): TiDataType.TI_DATA_TYPE_U32,
        dtype('uint64'): TiDataType.TI_DATA_TYPE_U64,
        dtype('float16'): TiDataType.TI_DATA_TYPE_F16,
        dtype('float32'): TiDataType.TI_DATA_TYPE_F32,
        dtype('float64'): TiDataType.TI_DATA_TYPE_F64
    }


def get_ndarray_ti_data_type(array: ndarray) -> TiDataType:
    return _TiTypeMap.ndarray_element[array.dtype]


def get_ti_argument_type(arg) -> TiArgumentType:
    return _TiTypeMap.kernel_argument.get(type(arg))


ctypes_data_type = {
    dtype('int8'): c_int8,
    dtype('int16'): c_int16,
    dtype('int32'): c_int32,
    dtype('int64'): c_int64,
    dtype('uint8'): c_uint8,
    dtype('uint16'): c_uint16,
    dtype('uint32'): c_uint32,
    dtype('uint64'): c_uint64,
    dtype('float16'): c_float,
    dtype('float32'): c_float,
    dtype('float64'): c_double
}


def get_ctypes_data_type(array: ndarray):
    return ctypes_data_type[array.dtype]
