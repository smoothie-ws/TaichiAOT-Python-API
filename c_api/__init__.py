"""Module providing Python wrapper for Taichi C-API."""
from ctypes import byref, create_string_buffer, string_at, cast, Array, c_void_p
from typing import List

from .taichi_c_utils import *
from .taichi_c_bindings import *

__all__ = [
    # aliases
    'TiBool', 'TiFlags',

    # definitions
    'TI_FALSE', 'TI_TRUE', 'TI_MAX_ARCH_COUNT', 'TI_NULL_HANDLE',

    # enumerations
    'TiError', 'TiArch', 'TiCapability', 'TiDataType', 'TiArgumentType',
    'TiMemoryUsageFlags', 'TiImageUsageFlags', 'TiImageDimension', 'TiImageLayout',
    'TiFormat', 'TiFilter', 'TiAddressMode',

    # handles
    'TiRuntime', 'TiAotModule', 'TiMemory', 'TiImage',
    'TiKernel', 'TiComputeGraph', 'TiSampler',

    # structures
    'TiCapabilityLevelInfo', 'TiMemoryAllocateInfo', 'TiMemorySlice', 'TiNdShape',
    'TiNdArray', 'TiImageOffset', 'TiImageExtent', 'TiImageAllocateInfo', 'TiImageSlice',
    'TiSamplerCreateInfo', 'TiTexture', 'TiScalarValue', 'TiScalar', 'TiTensorValue',
    'TiTensorValueWithLength', 'TiTensor', 'TiArgumentValue', 'TiArgument', 'TiNamedArgument',

    # functions
    'ti_get_version', 'ti_get_available_archs',
    'ti_get_last_error', 'ti_set_last_error',
    'ti_create_runtime', 'ti_destroy_runtime',
    'ti_load_aot_module', 'ti_create_aot_module', 'ti_destroy_aot_module',
    'ti_get_aot_module_kernel', 'ti_get_aot_module_compute_graph',
    'ti_launch_kernel', 'ti_launch_compute_graph',
    'ti_allocate_memory', 'ti_free_memory', 'ti_map_memory', 'ti_unmap_memory',
    'ti_allocate_image', 'ti_free_image',
    'ti_create_sampler', 'ti_destroy_sampler',
    'ti_copy_memory_device_to_device', 'ti_copy_image_device_to_device',
    'ti_track_image_ext', 'ti_transition_image',
    'ti_flush', 'ti_wait'
    ]


# Error Handling
def ti_get_version() -> c_uint32:
    """Get the current taichi version."""

    return c_ti_get_version()


def ti_get_last_error(size: int) -> tuple[str, int]:
    """Gets the last error raised by Taichi C-API invocations.
     Returns the semantical error message and error code."""

    message_size = c_uint64(size)  # Size of textual error message in `function.get_last_error.message`

    # Ignored when message_size is 0.
    message_buffer = create_string_buffer(message_size.value)  # Text buffer for the textual error message.

    error_code = c_ti_get_last_error(byref(message_size), message_buffer)
    error_message = string_at(message_buffer, message_size.value).decode('utf-8')

    return error_message, error_code


def ti_set_last_error(error: TiError, message: str) -> None:
    """Sets the provided error as the last error raised by Taichi C-API invocations."""

    c_ti_set_last_error(error, message.encode('utf-8'))


# Memory Operations
def ti_allocate_memory(runtime: TiRuntime, allocate_info: TiMemoryAllocateInfo) -> TiMemory:
    """Allocate memory on the TiRuntime."""

    address = c_ti_allocate_memory(runtime, byref(allocate_info))
    return cast(address, TiMemory)


def ti_free_memory(runtime: TiRuntime, memory: TiMemory) -> None:
    """Free allocated memory on the TiRuntime."""

    c_ti_free_memory(runtime, memory)


def ti_map_memory(runtime: TiRuntime, memory: TiMemory) -> c_void_p:
    """Map allocated memory on the TiRuntime."""

    return c_ti_map_memory(runtime, memory)


def ti_unmap_memory(runtime: TiRuntime, memory: TiMemory) -> None:
    """Unmap allocated memory on the TiRuntime."""

    c_ti_unmap_memory(runtime, memory)


def ti_get_available_archs() -> tuple[c_uint32, Array[int]]:
    """Get available architectures on the TiRuntime."""

    arch_count = c_uint32(TI_MAX_ARCH_COUNT)
    arch_list = (c_uint32 * TI_MAX_ARCH_COUNT)()

    c_ti_get_available_archs(byref(arch_count), arch_list)

    return arch_count, arch_list


def ti_allocate_image(runtime: TiRuntime, allocate_info: TiImageAllocateInfo) -> TiImage:
    """Allocate an image on the TiRuntime."""

    return c_ti_allocate_image(runtime, byref(allocate_info))


def ti_free_image(runtime: TiRuntime, image: TiImage) -> None:
    """Free an allocated image on the TiRuntime."""

    c_ti_free_image(runtime, image)


def ti_create_sampler(runtime: TiRuntime, create_info: TiSamplerCreateInfo) -> TiSampler:
    """Create a sampler on the TiRuntime."""

    address = c_ti_create_sampler(runtime, byref(create_info))
    return cast(address, TiSampler)


def ti_destroy_sampler(runtime: TiRuntime, sampler: TiSampler) -> None:
    """Destroy a sampler on the TiRuntime."""

    c_ti_destroy_sampler(runtime, sampler)


def ti_copy_memory_device_to_device(runtime: TiRuntime, src: TiMemorySlice, dst: TiMemorySlice) -> None:
    """Copy memory from one device to another on the TiRuntime."""

    c_ti_copy_memory_device_to_device(runtime, byref(src), byref(dst))


def ti_copy_image_device_to_device(runtime: TiRuntime, src: TiImageSlice, dst: TiImageSlice) -> None:
    """Copy an image from one device to another on the TiRuntime."""

    c_ti_copy_image_device_to_device(runtime, byref(src), byref(dst))


def ti_track_image_ext(runtime: TiRuntime, image: TiImage, layout: TiImageLayout) -> None:
    """Track an image on the TiRuntime with an extended layout."""

    c_ti_track_image_ext(runtime, image, layout)


def ti_transition_image(runtime: TiRuntime, image: TiImage, layout: TiImageLayout) -> None:
    """Transition an image on the TiRuntime to a new layout."""

    c_ti_transition_image(runtime, image, layout)


def ti_launch_kernel(runtime: TiRuntime, kernel: TiKernel, num_args: int, args: List[TiArgument]) -> None:
    """Launches a Taichi kernel with the provided arguments.
    The arguments must have the same count and types in the same order as in the source code.

    Parameters:
    - runtime (Type: TiRuntime): The runtime on which the kernel will be launched.
    - kernel (Type: TiKernel): The kernel to be launched.
    - num_args (Type: int): Number of kernel arguments.
    - args (Type: List[TiArgument]): List of kernel arguments.

    Returns: None"""

    c_ti_launch_kernel(runtime, kernel, num_args, (TiArgument * num_args)(*args))


def ti_launch_compute_graph(runtime: TiRuntime, graph: TiComputeGraph,
                            num_args: int, named_args: List[TiNamedArgument]) -> None:
    """Launch a compute graph on the TiRuntime."""

    c_ti_launch_compute_graph(runtime, graph, num_args, (TiNamedArgument * num_args)(*named_args))


def ti_flush(runtime: TiRuntime) -> None:
    """Flush operations on the TiRuntime."""

    c_ti_flush(runtime)


def ti_wait(runtime: TiRuntime) -> None:
    """Wait for operations on the TiRuntime to complete."""

    c_ti_wait(runtime)


def ti_create_runtime(arch: TiArch, device: int) -> TiRuntime:
    """Creates a Taichi Runtime with the specified TiArch."""

    address = c_ti_create_runtime(arch, device)
    return cast(address, TiRuntime)


def ti_destroy_runtime(runtime: TiRuntime) -> None:
    """Destroys a Taichi Runtime."""

    c_ti_destroy_runtime(runtime)


def ti_load_aot_module(runtime: TiRuntime, filepath: str) -> TiAotModule:
    """Load an AOT module from a file on the TiRuntime."""

    address = c_ti_load_aot_module(runtime, filepath.encode('utf-8'))
    return cast(address, TiAotModule)


def ti_create_aot_module(runtime: TiRuntime, data: c_void_p, size: int) -> c_void_p:
    """Create an AOT module on the TiRuntime from data."""

    return c_ti_create_aot_module(runtime, data, size)


def ti_destroy_aot_module(module: TiAotModule) -> None:
    """Destroy an AOT module on the TiRuntime."""

    c_ti_destroy_aot_module(module)


def ti_get_aot_module_kernel(module: TiAotModule, kernel_name: str) -> TiKernel:
    """Get a kernel from an AOT module on the TiRuntime."""

    address = c_ti_get_aot_module_kernel(module, kernel_name.encode('utf-8'))
    return cast(address, TiKernel)


def ti_get_aot_module_compute_graph(module: TiAotModule, graph_name: str) -> TiComputeGraph:
    """Get a compute graph from an AOT module on the TiRuntime."""

    address = c_ti_get_aot_module_compute_graph(module, graph_name.encode('utf-8'))
    return cast(address, TiComputeGraph)
