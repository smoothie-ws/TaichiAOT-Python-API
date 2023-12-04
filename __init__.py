from ctypes import byref, create_string_buffer, string_at, cast
from typing import List, Tuple

from .aliases import *
from .definitions import *
from .enumerations import *
from .functions import *
from .handles import *
from .structures import *


def get_version() -> c_uint32:
    """Description placeholder"""

    return ti_get_version()


def get_last_error() -> str:
    """Gets the last error raised by Taichi C-API invocations"""

    message_size = c_uint64(256)
    message_buffer = create_string_buffer(message_size.value)

    error_code = ti_get_last_error(byref(message_size), message_buffer)
    error_message = string_at(message_buffer, message_size.value).decode('utf-8')

    return f"Taichi C-API returned: {error_message}. Error code: {error_code}"


def create_runtime(arch: TiArch,
                   device: int) -> TiRuntime:
    """Description placeholder"""

    address = ti_create_runtime(arch, device)
    return cast(address, TiRuntime)


def get_available_archs() -> Tuple[List[c_uint32], List[TiArch]]:
    """Description placeholder"""

    arch_count = c_uint32(0)
    arch_list = (c_uint32 * 16)()

    ti_get_available_archs(byref(arch_count), arch_list)

    return list(arch_list[:arch_count.value]), [TiArch(arch) for arch in arch_list[:arch_count.value]]


def destroy_runtime(runtime: TiRuntime) -> None:
    """Description placeholder"""

    ti_destroy_runtime(runtime)


def set_last_error(error: TiError,
                   message: str) -> None:
    """Description placeholder"""

    ti_set_last_error(error, message.encode('utf-8'))


def allocate_memory(runtime: TiRuntime,
                    allocate_info: TiMemoryAllocateInfo) -> TiMemory:
    """Allocate memory and return a TiMemory pointer."""

    address = ti_allocate_memory(runtime, byref(allocate_info))
    return cast(address, TiMemory)


def free_memory(runtime: TiRuntime,
                memory: TiMemory) -> None:
    """Free the allocated memory."""

    ti_free_memory(runtime, memory)


def map_memory(runtime: TiRuntime,
               memory: TiMemory) -> c_void_p:
    """Map device memory to host-addressable space."""

    return ti_map_memory(runtime, memory)


def unmap_memory(runtime: TiRuntime,
                 memory: TiMemory) -> None:
    """Unmap device memory, making host-side changes visible to the device."""

    ti_unmap_memory(runtime, memory)


def allocate_image(runtime: TiRuntime,
                   allocate_info: TiImageAllocateInfo) -> c_void_p:
    """Description placeholder"""

    return ti_allocate_image(runtime, byref(allocate_info))


def free_image(runtime: TiRuntime,
               image: TiImage) -> None:
    """Description placeholder"""

    ti_free_image(runtime, image)


def create_sampler(runtime: TiRuntime,
                   create_info: TiSamplerCreateInfo) -> TiSampler:
    """Description placeholder"""

    address = ti_create_sampler(runtime, byref(create_info))
    return cast(address, TiSampler)


def destroy_sampler(runtime: TiRuntime,
                    sampler: TiSampler) -> None:
    """Description placeholder"""

    ti_destroy_sampler(runtime, sampler)


def copy_memory_device_to_device(runtime: TiRuntime,
                                 src: TiMemorySlice,
                                 dst: TiMemorySlice) -> None:
    """Description placeholder"""

    ti_copy_memory_device_to_device(runtime, byref(src), byref(dst))


def copy_image_device_to_device(runtime: TiRuntime,
                                src: TiImageSlice,
                                dst: TiImageSlice) -> None:
    """Description placeholder"""

    ti_copy_image_device_to_device(runtime, byref(src), byref(dst))


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


def launch_kernel(runtime: TiRuntime,
                  kernel: TiKernel,
                  num_args: int,
                  args: List[TiArgument]) -> None:
    """Description placeholder"""

    ti_launch_kernel(runtime, kernel, num_args, byref((TiArgument * num_args)(*args)))


def launch_compute_graph(runtime: TiRuntime,
                         graph: TiComputeGraph,
                         num_args: int,
                         named_args: List[TiNamedArgument]) -> None:
    """Description placeholder"""

    ti_launch_compute_graph(runtime, graph, num_args, (TiNamedArgument * num_args)(*named_args))


def flush(runtime: TiRuntime) -> None:
    """Description placeholder"""

    ti_flush(runtime)


def wait(runtime: TiRuntime) -> None:
    """Description placeholder"""

    ti_wait(runtime)


def load_aot_module(runtime: TiRuntime,
                    filepath: str) -> TiAotModule:
    """Description placeholder"""

    folder = dirname(abspath(__name__))
    aot_module_path: bytes = join(folder, filepath).encode('utf-8')

    address = ti_load_aot_module(runtime, aot_module_path)
    return cast(address, TiAotModule)


def create_aot_module(runtime: TiRuntime,
                      data: c_void_p,
                      size: int) -> c_void_p:
    """Description placeholder"""

    return ti_create_aot_module(runtime, data, size)


def destroy_aot_module(module: TiAotModule) -> None:
    """Description placeholder"""

    ti_destroy_aot_module(module)


def get_aot_module_kernel(module: TiAotModule,
                          kernel_name: str) -> TiKernel:
    """Description placeholder"""

    address = ti_get_aot_module_kernel(module, kernel_name.encode('utf-8'))
    return cast(address, TiKernel)


def get_aot_module_compute_graph(module: TiAotModule,
                                 graph_name: str) -> TiComputeGraph:
    """Description placeholder"""

    address = ti_get_aot_module_compute_graph(module, graph_name.encode('utf-8'))
    return cast(address, TiComputeGraph)
