from ctypes import c_int8, c_int16, c_int32, c_int64, c_uint8, c_uint16, c_uint32, c_uint64, c_float, c_double
import numpy as np

from .c_api import *

ti_data_type = {
    np.dtype('int8'): TiDataType.TI_DATA_TYPE_I8,
    np.dtype('int16'): TiDataType.TI_DATA_TYPE_I16,
    np.dtype('int32'): TiDataType.TI_DATA_TYPE_I32,
    np.dtype('int64'): TiDataType.TI_DATA_TYPE_I64,
    np.dtype('uint8'): TiDataType.TI_DATA_TYPE_U8,
    np.dtype('uint16'): TiDataType.TI_DATA_TYPE_U16,
    np.dtype('uint32'): TiDataType.TI_DATA_TYPE_U32,
    np.dtype('uint64'): TiDataType.TI_DATA_TYPE_U64,
    np.dtype('float16'): TiDataType.TI_DATA_TYPE_F16,
    np.dtype('float32'): TiDataType.TI_DATA_TYPE_F32,
    np.dtype('float64'): TiDataType.TI_DATA_TYPE_F64
}

ctypes_data_type = {
    np.dtype('int8'): c_int8,
    np.dtype('int16'): c_int16,
    np.dtype('int32'): c_int32,
    np.dtype('int64'): c_int64,
    np.dtype('uint8'): c_uint8,
    np.dtype('uint16'): c_uint16,
    np.dtype('uint32'): c_uint32,
    np.dtype('uint64'): c_uint64,
    np.dtype('float16'): c_float,
    np.dtype('float32'): c_float,
    np.dtype('float64'): c_double
}

taichi_argument_data_type = {
    int: TiArgumentType.TI_ARGUMENT_TYPE_I32,
    float: TiArgumentType.TI_ARGUMENT_TYPE_F32,
    np.ndarray: TiArgumentType.TI_ARGUMENT_TYPE_NDARRAY
}


def taichi_datatype(array: np.ndarray):
    return ti_data_type[array.dtype]


def ctypes_datatype(array: np.ndarray):
    return ctypes_data_type[array.dtype]
