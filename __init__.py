from ctypes import c_void_p

from .AotModule import aot_module
from .ComputeGraph import compute_graph
from .KernelArgument import kernel_argument
from .Kernel import kernel
from .Runtime import runtime
from .c_api import *
from .utils import *

__all__ = ['c_api',
           'get_version',
           'get_last_error',
           'set_last_error',
           'get_available_archs']


# Error Handling
def get_version() -> c_uint32:
    return ti_get_version()


def get_last_error(message_size: int = 256) -> str:
    error_message, error = ti_get_last_error(message_size)

    return f"Last error message: {error_message}. Error code: {error}. Details: {TiError.get_error_details(error)}"


def set_last_error(error: TiError, message: str) -> None:
    ti_set_last_error(error, message)


def get_available_archs() -> list[str]:
    """Gets a list of available archs on the current platform."""

    arch_count, arch_list = ti_get_available_archs()
    arch_values = [arch_list[i] for i in range(arch_count.value)]

    return [attr_name for attr_name in dir(TiArch) if
            not attr_name.startswith("__") and getattr(TiArch, attr_name) in arch_values]


def allocate_image(runtime: TiRuntime,
                   allocate_info: TiImageAllocateInfo) -> c_void_p:
    """Description placeholder"""

    return ti_allocate_image(runtime, allocate_info)


def free_image(runtime: TiRuntime,
               image: TiImage) -> None:
    """Description placeholder"""

    ti_free_image(runtime, image)


def create_sampler(runtime: TiRuntime,
                   create_info: TiSamplerCreateInfo) -> TiSampler:
    """Description placeholder"""

    return ti_create_sampler(runtime, create_info)


def destroy_sampler(runtime: TiRuntime,
                    sampler: TiSampler) -> None:
    """Description placeholder"""

    ti_destroy_sampler(runtime, sampler)


def copy_memory_device_to_device(runtime: TiRuntime,
                                 src: TiMemorySlice,
                                 dst: TiMemorySlice) -> None:
    """Description placeholder"""

    ti_copy_memory_device_to_device(runtime, src, dst)


def copy_image_device_to_device(runtime: TiRuntime,
                                src: TiImageSlice,
                                dst: TiImageSlice) -> None:
    """Description placeholder"""

    ti_copy_image_device_to_device(runtime, src, dst)


def track_image_ext(runtime: TiRuntime,
                    image: TiImage,
                    layout: TiImageLayout) -> None:
    """Description placeholder"""

    ti_track_image_ext(runtime, image, layout)


def transition_image(runtime: TiRuntime,
                     image: TiImage,
                     layout: TiImageLayout) -> None:
    """Description placeholder"""

    ti_transition_image(runtime, image, layout)
