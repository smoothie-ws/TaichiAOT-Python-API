from ctypes import c_int8, c_int16, c_int32, c_int64, c_uint8, c_uint16, c_uint32, c_uint64, c_float, c_double, c_void_p
import numpy as np

from taichiAOT import c_api

__all__ = ['c_api',
           'get_version',
           'get_last_error',
           'set_last_error',
           'get_available_archs']

ti_data_type = {
    np.dtype('int8'): c_api.TiDataType.TI_DATA_TYPE_I8,
    np.dtype('int16'): c_api.TiDataType.TI_DATA_TYPE_I16,
    np.dtype('int32'): c_api.TiDataType.TI_DATA_TYPE_I32,
    np.dtype('int64'): c_api.TiDataType.TI_DATA_TYPE_I64,
    np.dtype('uint8'): c_api.TiDataType.TI_DATA_TYPE_U8,
    np.dtype('uint16'): c_api.TiDataType.TI_DATA_TYPE_U16,
    np.dtype('uint32'): c_api.TiDataType.TI_DATA_TYPE_U32,
    np.dtype('uint64'): c_api.TiDataType.TI_DATA_TYPE_U64,
    np.dtype('float16'): c_api.TiDataType.TI_DATA_TYPE_F16,
    np.dtype('float32'): c_api.TiDataType.TI_DATA_TYPE_F32,
    np.dtype('float64'): c_api.TiDataType.TI_DATA_TYPE_F64
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
    int: c_api.TiArgumentType.TI_ARGUMENT_TYPE_I32,
    float: c_api.TiArgumentType.TI_ARGUMENT_TYPE_F32,
    np.ndarray: c_api.TiArgumentType.TI_ARGUMENT_TYPE_NDARRAY
}


def taichi_datatype(array: np.ndarray):
    return ti_data_type[array.dtype]


def ctypes_datatype(array: np.ndarray):
    return ctypes_data_type[array.dtype]


def get_version() -> c_uint32:
    return c_api.ti_get_version()


def get_last_error(message_size: int = 256) -> None:
    error_message, error_code = c_api.ti_get_last_error(message_size)

    if error_code != 0:
        raise RuntimeError(f"{error_message}. \n"
                           f"Error code: {error_code}. Details: {c_api.TiError.get_error_details(error_code)}")


def set_last_error(error: c_api.TiError, message: str) -> None:
    c_api.ti_set_last_error(error, message)


def get_available_archs() -> list[str]:
    """Gets a list of available archs on the current platform."""

    arch_count, arch_list = c_api.ti_get_available_archs()
    arch_values = [arch_list[i] for i in range(arch_count.value)]

    return [attr_name for attr_name in dir(c_api.TiArch) if
            not attr_name.startswith("__") and getattr(c_api.TiArch, attr_name) in arch_values]


def allocate_image(ti_runtime: c_api.TiRuntime,
                   allocate_info: c_api.TiImageAllocateInfo) -> c_void_p:
    """Description placeholder"""

    return c_api.ti_allocate_image(ti_runtime, allocate_info)


def free_image(ti_runtime: c_api.TiRuntime,
               image: c_api.TiImage) -> None:
    """Description placeholder"""

    c_api.ti_free_image(ti_runtime, image)


def copy_memory_device_to_device(ti_runtime: c_api.TiRuntime,
                                 src: c_api.TiMemorySlice,
                                 dst: c_api.TiMemorySlice) -> None:
    """Description placeholder"""

    c_api.ti_copy_memory_device_to_device(ti_runtime, src, dst)


def copy_image_device_to_device(ti_runtime: c_api.TiRuntime,
                                src: c_api.TiImageSlice,
                                dst: c_api.TiImageSlice) -> None:
    """Description placeholder"""

    c_api.ti_copy_image_device_to_device(ti_runtime, src, dst)


def track_image_ext(ti_runtime: c_api.TiRuntime,
                    image: c_api.TiImage,
                    layout: c_api.TiImageLayout) -> None:
    """Description placeholder"""

    c_api.ti_track_image_ext(ti_runtime, image, layout)


def transition_image(ti_runtime: c_api.TiRuntime,
                     image: c_api.TiImage,
                     layout: c_api.TiImageLayout) -> None:
    """Description placeholder"""

    c_api.ti_transition_image(ti_runtime, image, layout)
