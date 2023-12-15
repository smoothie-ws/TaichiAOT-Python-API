"""Module providing Python bindings for TiRuntime functions."""

from ctypes import byref, create_string_buffer, string_at, cast, Array, c_void_p, c_uint32
from typing import List, Any, Tuple

from .TiDefinitions import *
from .TiFunctions import *
from .TiHandles import *
from .TiStructures import *

__all__ = ['_py_ti_get_version',
           '_py_ti_get_last_error',
           '_py_ti_set_last_error',
           '_py_ti_create_runtime',
           '_py_ti_allocate_memory',
           '_py_ti_free_memory',
           '_py_ti_map_memory',
           '_py_ti_unmap_memory',
           '_py_ti_get_available_archs',
           '_py_ti_destroy_runtime',
           '_py_ti_allocate_image',
           '_py_ti_free_image',
           '_py_ti_create_sampler',
           '_py_ti_destroy_sampler',
           '_py_ti_copy_memory_device_to_device',
           '_py_ti_copy_image_device_to_device',
           '_py_ti_track_image_ext',
           '_py_ti_transition_image',
           '_py_ti_launch_kernel',
           '_py_ti_launch_compute_graph',
           '_py_ti_flush',
           '_py_ti_wait',
           '_py_ti_load_aot_module',
           '_py_ti_create_aot_module',
           '_py_ti_destroy_aot_module',
           '_py_ti_get_aot_module_kernel',
           '_py_ti_get_aot_module_compute_graph']


# Error Handling
def _py_ti_get_version() -> c_uint32:
    """Get the current taichi version."""

    return ti_get_version()


def _py_ti_get_last_error(size: int) -> tuple[str, int]:
    """Gets the last error raised by Taichi C-API invocations.
     Returns the semantical error message and error code."""

    message_size = c_uint64(size)  # Size of textual error message in `function.get_last_error.message`

    # Ignored when message_size is 0.
    message_buffer = create_string_buffer(message_size.value)  # Text buffer for the textual error message.

    error_code = ti_get_last_error(byref(message_size), message_buffer)
    error_message = string_at(message_buffer, message_size.value).decode('utf-8')

    return error_message, error_code


def _py_ti_set_last_error(error: TiError, message: str) -> None:
    """Sets the provided error as the last error raised by Taichi C-API invocations."""

    ti_set_last_error(error, message.encode('utf-8'))


# Memory Operations
def _py_ti_allocate_memory(runtime: TiRuntime, allocate_info: TiMemoryAllocateInfo) -> TiMemory:
    """Allocate memory on the TiRuntime."""

    address = ti_allocate_memory(runtime, byref(allocate_info))
    return cast(address, TiMemory)


def _py_ti_free_memory(runtime: TiRuntime, memory: TiMemory) -> None:
    """Free allocated memory on the TiRuntime."""

    ti_free_memory(runtime, memory)


def _py_ti_map_memory(runtime: TiRuntime, memory: TiMemory) -> c_void_p:
    """Map allocated memory on the TiRuntime."""

    return ti_map_memory(runtime, memory)


def _py_ti_unmap_memory(runtime: TiRuntime, memory: TiMemory) -> None:
    """Unmap allocated memory on the TiRuntime."""

    ti_unmap_memory(runtime, memory)


def _py_ti_get_available_archs() -> tuple[c_uint32, Array[int]]:
    """Get available architectures on the TiRuntime."""

    arch_count = c_uint32(TI_MAX_ARCH_COUNT)
    arch_list = (c_uint32 * TI_MAX_ARCH_COUNT)()

    ti_get_available_archs(byref(arch_count), arch_list)

    return arch_count, arch_list


def _py_ti_allocate_image(runtime: TiRuntime, allocate_info: TiImageAllocateInfo) -> TiImage:
    """Allocate an image on the TiRuntime."""

    return ti_allocate_image(runtime, byref(allocate_info))


def _py_ti_free_image(runtime: TiRuntime, image: TiImage) -> None:
    """Free an allocated image on the TiRuntime."""

    ti_free_image(runtime, image)


def _py_ti_create_sampler(runtime: TiRuntime, create_info: TiSamplerCreateInfo) -> TiSampler:
    """Create a sampler on the TiRuntime."""

    address = ti_create_sampler(runtime, byref(create_info))
    return cast(address, TiSampler)


def _py_ti_destroy_sampler(runtime: TiRuntime, sampler: TiSampler) -> None:
    """Destroy a sampler on the TiRuntime."""

    ti_destroy_sampler(runtime, sampler)


def _py_ti_copy_memory_device_to_device(runtime: TiRuntime, src: TiMemorySlice, dst: TiMemorySlice) -> None:
    """Copy memory from one device to another on the TiRuntime."""

    ti_copy_memory_device_to_device(runtime, byref(src), byref(dst))


def _py_ti_copy_image_device_to_device(runtime: TiRuntime, src: TiImageSlice, dst: TiImageSlice) -> None:
    """Copy an image from one device to another on the TiRuntime."""

    ti_copy_image_device_to_device(runtime, byref(src), byref(dst))


def _py_ti_track_image_ext(runtime: TiRuntime, image: TiImage, layout: TiImageLayout) -> None:
    """Track an image on the TiRuntime with an extended layout."""

    ti_track_image_ext(runtime, image, layout)


def _py_ti_transition_image(runtime: TiRuntime, image: TiImage, layout: TiImageLayout) -> None:
    """Transition an image on the TiRuntime to a new layout."""

    ti_transition_image(runtime, image, layout)


def _py_ti_launch_kernel(runtime: TiRuntime, kernel: TiKernel, num_args: int, args: List[TiArgument]) -> None:
    """Launches a Taichi kernel with the provided arguments.
    The arguments must have the same count and types in the same order as in the source code.

    Parameters:
    - runtime (Type: TiRuntime): The runtime on which the kernel will be launched.
    - kernel (Type: TiKernel): The kernel to be launched.
    - num_args (Type: int): Number of kernel arguments.
    - args (Type: List[TiArgument]): List of kernel arguments.

    Returns: None"""

    ti_launch_kernel(runtime, kernel, num_args, byref((TiArgument * num_args)(*args)))


def _py_ti_launch_compute_graph(runtime: TiRuntime, graph: TiComputeGraph,
                                num_args: int, named_args: List[TiNamedArgument]) -> None:
    """Launch a compute graph on the TiRuntime."""

    ti_launch_compute_graph(runtime, graph, num_args, (TiNamedArgument * num_args)(*named_args))


def _py_ti_flush(runtime: TiRuntime) -> None:
    """Flush operations on the TiRuntime."""

    ti_flush(runtime)


def _py_ti_wait(runtime: TiRuntime) -> None:
    """Wait for operations on the TiRuntime to complete."""

    ti_wait(runtime)


def _py_ti_create_runtime(arch: TiArch, device: int) -> TiRuntime:
    """Creates a Taichi Runtime with the specified TiArch."""

    address = ti_create_runtime(arch, device)
    return cast(address, TiRuntime)


def _py_ti_destroy_runtime(runtime: TiRuntime) -> None:
    """Destroys a Taichi Runtime."""

    ti_destroy_runtime(runtime)


def _py_ti_load_aot_module(runtime: TiRuntime, filepath: str) -> TiAotModule:
    """Load an AOT module from a file on the TiRuntime."""

    address = ti_load_aot_module(runtime, filepath.encode('utf-8'))
    return cast(address, TiAotModule)


def _py_ti_create_aot_module(runtime: TiRuntime, data: c_void_p, size: int) -> c_void_p:
    """Create an AOT module on the TiRuntime from data."""

    return ti_create_aot_module(runtime, data, size)


def _py_ti_destroy_aot_module(module: TiAotModule) -> None:
    """Destroy an AOT module on the TiRuntime."""

    ti_destroy_aot_module(module)


def _py_ti_get_aot_module_kernel(module: TiAotModule, kernel_name: str) -> TiKernel:
    """Get a kernel from an AOT module on the TiRuntime."""

    address = ti_get_aot_module_kernel(module, kernel_name.encode('utf-8'))
    return cast(address, TiKernel)


def _py_ti_get_aot_module_compute_graph(module: TiAotModule, graph_name: str) -> TiComputeGraph:
    """Get a compute graph from an AOT module on the TiRuntime."""

    address = ti_get_aot_module_compute_graph(module, graph_name.encode('utf-8'))
    return cast(address, TiComputeGraph)