from ctypes import c_void_p
from os.path import dirname, abspath, join
from typing import List

from .TiAliases import *
from .TiDefinitions import *
from .TiEnumerations import *
from .TiFunctions import *
from .TiHandles import *
from .TiStructures import *
from .TiWrapper import *

__all__ = ['TiAliases',
           'TiDefinitions',
           'TiEnumerations',
           'TiFunctions',
           'TiHandles',
           'TiStructures',
           'get_version',
           'get_last_error',
           'set_last_error',
           'create_runtime',
           'allocate_memory',
           'free_memory',
           'map_memory',
           'unmap_memory',
           'get_available_archs',
           'destroy_runtime',
           'allocate_image',
           'free_image',
           'create_sampler',
           'destroy_sampler',
           'copy_memory_device_to_device',
           'copy_image_device_to_device',
           'track_image_ext',
           'transition_image',
           'launch_kernel',
           'launch_compute_graph',
           'flush',
           'wait',
           'load_aot_module',
           'create_aot_module',
           'destroy_aot_module',
           'get_aot_module_kernel',
           'get_aot_module_compute_graph']


# Error Handling
def get_version() -> c_uint32:
    return _py_ti_get_version()


def get_last_error(message_size: int) -> str:
    error_message, error_code = _py_ti_get_last_error(message_size)

    return f"Taichi C-API returned: {error_message}. Error code: {error_code}"


def set_last_error(error: TiError, message: str) -> None:
    _py_ti_set_last_error(error, message)


# Memory Operations
def allocate_memory(runtime: TiRuntime, allocate_info: TiMemoryAllocateInfo) -> TiMemory:
    return _py_ti_allocate_memory(runtime, allocate_info)


def free_memory(runtime: TiRuntime, memory: TiMemory) -> None:
    _py_ti_free_memory(runtime, memory)


def map_memory(runtime: TiRuntime, memory: TiMemory) -> c_void_p:
    return _py_ti_map_memory(runtime, memory)


def unmap_memory(runtime: TiRuntime, memory: TiMemory) -> None:
    _py_ti_unmap_memory(runtime, memory)


def get_available_archs() -> list[TiArch]:
    """Gets a list of available archs on the current platform."""

    arch_count, arch_list = _py_ti_get_available_archs()
    arch_values = [arch_list[i] for i in range(arch_count.value)]

    return arch_values


def allocate_image(runtime: TiRuntime,
                   allocate_info: TiImageAllocateInfo) -> c_void_p:
    """Description placeholder"""

    return _py_ti_allocate_image(runtime, allocate_info)


def free_image(runtime: TiRuntime,
               image: TiImage) -> None:
    """Description placeholder"""

    _py_ti_free_image(runtime, image)


def create_sampler(runtime: TiRuntime,
                   create_info: TiSamplerCreateInfo) -> TiSampler:
    """Description placeholder"""

    return _py_ti_create_sampler(runtime, create_info)


def destroy_sampler(runtime: TiRuntime,
                    sampler: TiSampler) -> None:
    """Description placeholder"""

    _py_ti_destroy_sampler(runtime, sampler)


def copy_memory_device_to_device(runtime: TiRuntime,
                                 src: TiMemorySlice,
                                 dst: TiMemorySlice) -> None:
    """Description placeholder"""

    _py_ti_copy_memory_device_to_device(runtime, src, dst)


def copy_image_device_to_device(runtime: TiRuntime,
                                src: TiImageSlice,
                                dst: TiImageSlice) -> None:
    """Description placeholder"""

    _py_ti_copy_image_device_to_device(runtime, src, dst)


def track_image_ext(runtime: TiRuntime,
                    image: TiImage,
                    layout: TiImageLayout) -> None:
    """Description placeholder"""

    _py_ti_track_image_ext(runtime, image, layout)


def transition_image(runtime: TiRuntime,
                     image: TiImage,
                     layout: TiImageLayout) -> None:
    """Description placeholder"""

    _py_ti_transition_image(runtime, image, layout)


def launch_kernel(runtime: TiRuntime,
                  kernel: TiKernel,
                  args: List[TiArgument]) -> None:
    """Description placeholder"""

    _py_ti_launch_kernel(runtime, kernel, len(args), args)


def launch_compute_graph(runtime: TiRuntime,
                         graph: TiComputeGraph,
                         named_args: List[TiNamedArgument]) -> None:
    """Description placeholder"""

    _py_ti_launch_compute_graph(runtime, graph, len(named_args), named_args)


def flush(runtime: TiRuntime) -> None:
    """Description placeholder"""

    _py_ti_flush(runtime)


def wait(runtime: TiRuntime) -> None:
    """Description placeholder"""

    _py_ti_wait(runtime)


def load_aot_module(runtime: TiRuntime,
                    filepath: str) -> TiAotModule:
    """Description placeholder"""

    folder = dirname(abspath(__name__))
    aot_module_path = join(folder, filepath)

    return _py_ti_load_aot_module(runtime, aot_module_path)


def create_runtime(arch: TiArch,
                   device: int) -> TiRuntime:
    """Description placeholder"""

    return _py_ti_create_runtime(arch, device)


def destroy_runtime(runtime: TiRuntime) -> None:
    """Description placeholder"""

    _py_ti_destroy_runtime(runtime)


def create_aot_module(runtime: TiRuntime,
                      data: c_void_p,
                      size: int) -> c_void_p:
    """Description placeholder"""

    return _py_ti_create_aot_module(runtime, data, size)


def destroy_aot_module(module: TiAotModule) -> None:
    """Description placeholder"""

    _py_ti_destroy_aot_module(module)


def get_aot_module_kernel(module: TiAotModule,
                          kernel_name: str) -> TiKernel:
    """Description placeholder"""

    return _py_ti_get_aot_module_kernel(module, kernel_name)


def get_aot_module_compute_graph(module: TiAotModule,
                                 graph_name: str) -> TiComputeGraph:
    """Description placeholder"""

    return _py_ti_get_aot_module_compute_graph(module, graph_name)