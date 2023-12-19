from ctypes import c_void_p

from .c_api import *


def get_version() -> int:
    return ti_get_version()


def get_last_error(message_size: int = 256) -> str:
    error_message, error_code = ti_get_last_error(message_size)

    if error_code != 0:
        raise RuntimeError(f"{error_message}. "
                           f"{TiError.get_error_details(error_code)}\n"
                           f"TiError code: {error_code}.")

    return f"{error_message}. Error code: {error_code}."


def set_last_error(error: TiError, message: str) -> None:
    ti_set_last_error(error, message)


def get_available_archs() -> list[str]:
    """Gets a list of available archs on the current platform."""

    arch_count, arch_list = ti_get_available_archs()
    arch_values = [arch_list[i] for i in range(arch_count.value)]

    return [attr_name for attr_name in dir(TiArch) if
            not attr_name.startswith("__")
            and getattr(TiArch, attr_name) in arch_values]


def allocate_image(ti_runtime: TiRuntime,
                   allocate_info: TiImageAllocateInfo) -> c_void_p:
    """Description placeholder"""

    return ti_allocate_image(ti_runtime, allocate_info)


def free_image(ti_runtime: TiRuntime,
               image: TiImage) -> None:
    """Description placeholder"""

    ti_free_image(ti_runtime, image)


def copy_memory_device_to_device(ti_runtime: TiRuntime,
                                 src: TiMemorySlice,
                                 dst: TiMemorySlice) -> None:
    """Description placeholder"""

    ti_copy_memory_device_to_device(ti_runtime, src, dst)


def copy_image_device_to_device(ti_runtime: TiRuntime,
                                src: TiImageSlice,
                                dst: TiImageSlice) -> None:
    """Description placeholder"""

    ti_copy_image_device_to_device(ti_runtime, src, dst)


def track_image_ext(ti_runtime: TiRuntime,
                    image: TiImage,
                    layout: TiImageLayout) -> None:
    """Description placeholder"""

    ti_track_image_ext(ti_runtime, image, layout)


def transition_image(ti_runtime: TiRuntime,
                     image: TiImage,
                     layout: TiImageLayout) -> None:
    """Description placeholder"""

    ti_transition_image(ti_runtime, image, layout)
