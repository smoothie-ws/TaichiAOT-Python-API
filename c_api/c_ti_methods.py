from ctypes import (Array, byref, create_string_buffer,
                    string_at, cast, c_void_p)
from typing import List

from ._api_loader import C_API
from .c_ti_enums import *
from .c_ti_structs import *

TAICHI_C_API = C_API()
assert TAICHI_C_API.loaded

TI_FALSE = 0
TI_TRUE = 1
TI_NULL_HANDLE = 0
TI_MAX_ARCH_COUNT = 16

__all__ = [
    # aliases
    'TiBool', 'TiFlags',

    # definitions
    'TI_FALSE', 'TI_TRUE', 'TI_MAX_ARCH_COUNT', 'TI_NULL_HANDLE',

    # enumerations
    'TiError', 'TiArch', 'TiCapability', 'TiDataType', 'TiArgumentType',
    'TiMemoryUsageFlags', 'TiImageUsageFlags', 'TiImageDimension',
    'TiImageLayout', 'TiFormat', 'TiFilter', 'TiAddressMode',

    # handles
    'TiRuntime', 'TiAotModule', 'TiMemory', 'TiImage',
    'TiKernel', 'TiComputeGraph', 'TiSampler',

    # structures
    'TiCapabilityLevelInfo', 'TiMemoryAllocateInfo', 'TiMemorySlice',
    'TiNdShape', 'TiNdArray', 'TiImageOffset', 'TiImageExtent',
    'TiImageAllocateInfo', 'TiImageSlice', 'TiSamplerCreateInfo',
    'TiTexture', 'TiScalarValue', 'TiScalar', 'TiTensorValue',
    'TiTensorValueWithLength', 'TiTensor', 'TiArgumentValue',
    'TiArgument', 'TiNamedArgument',

    # methods
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


def ti_get_version() -> int:
    """Get the current taichi version."""

    return TAICHI_C_API.ti_get_version()


def ti_get_available_archs() -> tuple[c_uint32, Array[TiArch]]:
    """Gets a list of available archs on the current platform.

    An arch is only available if:

    - The Runtime library is compiled with its support;
    - The current platform is installed with a capable hardware or an emulation software.

    An available arch has at least one device available,
    i.e., device index 0 is always available.

    If an arch is not available on the current platform,
    a call to ti_create_runtime with that arch is guaranteed failing.

    **WARNING** Please also note that the order or returned archs is undefined.
    """

    arch_count = c_uint32(TI_MAX_ARCH_COUNT)
    arch_list = (c_uint32 * TI_MAX_ARCH_COUNT)()

    TAICHI_C_API.ti_get_available_archs(byref(arch_count), arch_list)

    return arch_count, arch_list


def ti_get_last_error(message_size: int) -> tuple[str, int]:
    """Gets the last error raised by Taichi C-API invocations.

     Returns the semantic error message and error code.

    :param message_size: `Size of textual error message in message`
    """

    size = c_uint64(message_size)
    message_buffer = create_string_buffer(size.value)

    error_code = TAICHI_C_API.ti_get_last_error(byref(size),
                                                message_buffer)
    error_message = string_at(message_buffer, size.value).decode(
        'utf-8')

    return error_message, error_code


def ti_set_last_error(error: TiError, message: str) -> None:
    """Sets the provided error as the last error raised by Taichi C-API
    invocations.

    :param error: `Semantic error code.`
    :param message: `A null-terminated string of the textual
     error message or nullptr for empty error message.`
    """

    TAICHI_C_API.ti_set_last_error(error, message.encode('utf-8'))


def ti_allocate_memory(runtime: TiRuntime,
                       allocate_info: TiMemoryAllocateInfo) -> TiMemory:
    """Allocates a contiguous device memory with provided parameters.

    Return:
         A TiMemory instance.
    """

    address = TAICHI_C_API.ti_allocate_memory(runtime,
                                              byref(allocate_info))
    return cast(address, TiMemory)


def ti_free_memory(runtime: TiRuntime, memory: TiMemory) -> None:
    """Frees a memory allocation."""

    TAICHI_C_API.ti_free_memory(runtime, memory)


def ti_map_memory(runtime: TiRuntime, memory: TiMemory) -> TiMemory:
    """Maps a device memory to a host-addressable space.

    You **must** ensure that the device is not being used by any device
    command before the mapping.
    """

    return TAICHI_C_API.ti_map_memory(runtime, memory)


def ti_unmap_memory(runtime: TiRuntime, memory: TiMemory) -> None:
    """Unmaps a device memory and makes any host-side changes
    about the memory visible to the device.

    You **must** ensure that there is no further access to the
    previously mapped host-addressable space.
    """

    TAICHI_C_API.ti_unmap_memory(runtime, memory)


def ti_allocate_image(runtime: TiRuntime,
                      allocate_info: TiImageAllocateInfo) -> TiImage:
    """Allocates a device image with provided parameters.

    Return:
         A TiImage instance.
    """

    return TAICHI_C_API.ti_allocate_image(runtime, byref(allocate_info))


def ti_free_image(runtime: TiRuntime, image: TiImage) -> None:
    """Frees an image allocation."""

    TAICHI_C_API.ti_free_image(runtime, image)


def ti_create_sampler(runtime: TiRuntime,
                      create_info: TiSamplerCreateInfo) -> TiSampler:
    """Creates a sampler.

    Args:
        runtime (TiRuntime): The Taichi runtime instance.
        create_info (TiSamplerCreateInfo): Parameters for creating a sampler.

    Returns:
        TiSampler: The created sampler.
    """

    address = TAICHI_C_API.ti_create_sampler(runtime, byref(create_info))
    return cast(address, TiSampler)


def ti_destroy_sampler(runtime: TiRuntime, sampler: TiSampler) -> None:
    """Destroys a sampler.

    Args:
        runtime (TiRuntime): The Taichi runtime instance.
        sampler (TiSampler): The sampler to be destroyed.
    """

    TAICHI_C_API.ti_destroy_sampler(runtime, sampler)


def ti_copy_memory_device_to_device(runtime: TiRuntime, src: TiMemorySlice,
                                    dst: TiMemorySlice) -> None:
    """Copies the data in a contiguous subsection of the device memory
    to another subsection.

    The two subsections must not overlap.
    """

    TAICHI_C_API.ti_copy_memory_device_to_device(runtime, byref(src),
                                                 byref(dst))


def ti_copy_image_device_to_device(runtime: TiRuntime, src: TiImageSlice,
                                   dst: TiImageSlice) -> None:
    """Copies the image data in a contiguous subsection of the
    device image to another subsection.

    The two subsections *must not* overlap."""

    TAICHI_C_API.ti_copy_image_device_to_device(runtime, byref(src),
                                                byref(dst))


def ti_track_image_ext(runtime: TiRuntime, image: TiImage,
                       layout: TiImageLayout) -> None:
    """Tracks the device image with the provided image layout.

    Because Taichi tracks image layouts internally, it is *only* useful
    to inform Taichi that the image is transitioned to a new layout
    by external procedures.
    """

    TAICHI_C_API.ti_track_image_ext(runtime, image, layout)


def ti_transition_image(runtime: TiRuntime, image: TiImage,
                        layout: TiImageLayout) -> None:
    """Transitions the image to the provided image layout.

     Because Taichi tracks image layouts internally, it is *only* useful
     to enforce an image layout for external procedures to use.
     """

    TAICHI_C_API.ti_transition_image(runtime, image, layout)


def ti_launch_kernel(runtime: TiRuntime,
                     kernel: TiKernel,
                     num_args: int,
                     args: List[TiArgument]) -> None:
    """Launches a Taichi kernel with the provided arguments.

    The arguments **must** have the same count and types in the same order
    as in the source code.
    """

    TAICHI_C_API.ti_launch_kernel(runtime, kernel, num_args,
                                  (TiArgument * num_args)(*args))


def ti_launch_compute_graph(runtime: TiRuntime, graph: TiComputeGraph,
                            num_args: int,
                            named_args: List[TiNamedArgument]) -> None:
    """Launches a Taichi compute graph with provided named arguments.

    The named arguments **must** have the same count, names, and types
    as in the source code."""

    TAICHI_C_API.ti_launch_compute_graph(runtime, graph, num_args,
                                         (TiNamedArgument * num_args)(*named_args))


def ti_flush(runtime: TiRuntime) -> None:
    """Submits all previously invoked device commands to the offload device
    for execution.
    """

    TAICHI_C_API.ti_flush(runtime)


def ti_wait(runtime: TiRuntime) -> None:
    """Waits until all previously invoked device commands are executed.

     Any invoked command that has not been submitted is submitted first.
     """

    TAICHI_C_API.ti_wait(runtime)


def ti_create_runtime(arch: TiArch, device: int) -> TiRuntime:
    """Creates a Taichi Runtime with the specified TiArch.

    Return:
        a TiRuntime instance.
    """

    address = TAICHI_C_API.ti_create_runtime(arch, device)
    return cast(address, TiRuntime)


def ti_destroy_runtime(runtime: TiRuntime) -> None:
    """Destroys a Taichi Runtime."""

    TAICHI_C_API.ti_destroy_runtime(runtime)


def ti_set_runtime_capabilities_ext(runtime: TiRuntime,
                                    capabilities: List[
                                        TiCapabilityLevelInfo]) -> None:
    """Force override the list of available capabilities in the runtime instance.

    Args:
        runtime: A TiRuntime instance.
        capabilities: A list of TiCapabilityLevelInfo instances.
    """

    capability_count = len(capabilities)
    capabilities_array = (TiCapabilityLevelInfo * capability_count)(*capabilities)

    TAICHI_C_API.ti_set_runtime_capabilities_ext(runtime,
                                                 capability_count,
                                                 capabilities_array)


def ti_get_runtime_capabilities(runtime: TiRuntime) -> List[
    TiCapabilityLevelInfo]:
    """Gets all capabilities available on the runtime instance.

    Args:
        runtime: A TiRuntime instance.

    Returns:
        A list of TiCapabilityLevelInfo instances.
    """

    capability_count = c_uint32()
    TAICHI_C_API.ti_get_runtime_capabilities(runtime,
                                             byref(capability_count), None)

    capabilities_array = (TiCapabilityLevelInfo * capability_count.value)()
    TAICHI_C_API.ti_get_runtime_capabilities(runtime,
                                             byref(capability_count),
                                             capabilities_array)

    return list(capabilities_array)


def ti_load_aot_module(runtime: TiRuntime, filepath: str) -> TiAotModule:
    """Loads a pre-compiled AOT module from the file system.

    Returns TI_NULL_HANDLE if the runtime fails to load the AOT module
    from the specified path.

    Return:
        a TiAotModule instance.
    """

    address = TAICHI_C_API.ti_load_aot_module(runtime,filepath.encode('utf-8'))
    return cast(address, TiAotModule)


def ti_create_aot_module(runtime: TiRuntime, tcm: c_void_p,
                         size: int) -> TiAotModule:
    """Creates a pre-compiled AOT module from TCM data.

     Returns TI_NULL_HANDLE if the runtime fails to create the AOT module
     from TCM data.

     Return:
        a TiAotModule instance.
     """

    return TAICHI_C_API.ti_create_aot_module(runtime, tcm, size)


def ti_destroy_aot_module(module: TiAotModule) -> None:
    """Destroys a loaded AOT module and releases all related resources."""

    TAICHI_C_API.ti_destroy_aot_module(module)


def ti_get_aot_module_kernel(module: TiAotModule,
                             kernel_name: str) -> TiKernel:
    """Retrieves a pre-compiled Taichi kernel from the AOT module.

    Returns TI_NULL_HANDLE if the module does not have a kernel
    of the specified name.

    Return:
        a TiKernel instance.
    """

    address = TAICHI_C_API.ti_get_aot_module_kernel(module, kernel_name.encode('utf-8'))
    return cast(address, TiKernel)


def ti_get_aot_module_compute_graph(module: TiAotModule,
                                    graph_name: str) -> TiComputeGraph:
    """Retrieves a pre-compiled compute graph from the AOT module.

    Returns TI_NULL_HANDLE if the module does not have a compute graph
    of the specified name.

    Return:
        a TiComputeGraph instance.
    """

    address = TAICHI_C_API.ti_get_aot_module_compute_graph(module, graph_name.encode('utf-8'))
    return cast(address, TiComputeGraph)
