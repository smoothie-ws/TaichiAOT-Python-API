from ctypes import CDLL, POINTER, c_void_p
from os.path import dirname, join, abspath

from .TiHandles import *
from .TiStructures import *

_current_folder = dirname(abspath(__file__))
_taichi_lib_path = join(_current_folder, 'taichi_c_api.dll')
_taichi_lib = CDLL(_taichi_lib_path)

__all__ = ['ti_get_version',
           'ti_get_last_error',
           'ti_set_last_error',
           'ti_create_runtime',
           'ti_allocate_memory',
           'ti_free_memory',
           'ti_map_memory',
           'ti_unmap_memory',
           'ti_get_available_archs',
           'ti_destroy_runtime',
           'ti_allocate_image',
           'ti_free_image',
           'ti_create_sampler',
           'ti_destroy_sampler',
           'ti_copy_memory_device_to_device',
           'ti_copy_image_device_to_device',
           'ti_track_image_ext',
           'ti_transition_image',
           'ti_launch_kernel',
           'ti_launch_compute_graph',
           'ti_flush',
           'ti_wait',
           'ti_load_aot_module',
           'ti_create_aot_module',
           'ti_destroy_aot_module',
           'ti_get_aot_module_kernel',
           'ti_get_aot_module_compute_graph']

# Versioning and capability
ti_get_version = _taichi_lib.ti_get_version
ti_get_version.argtypes = None
ti_get_version.restype = c_uint32

ti_get_available_archs = _taichi_lib.ti_get_available_archs
ti_get_available_archs.argtypes = None
ti_get_available_archs.restype = None

ti_get_last_error = _taichi_lib.ti_get_last_error
ti_get_last_error.argtypes = [POINTER(c_uint64), c_char_p]
ti_get_last_error.restype = TiError

ti_set_last_error = _taichi_lib.ti_set_last_error
ti_set_last_error.argtypes = [c_uint32, c_char_p]
ti_set_last_error.restype = None

# Runtime
ti_create_runtime = _taichi_lib.ti_create_runtime
ti_create_runtime.argtypes = [TiArch, c_uint32]
ti_create_runtime.restype = TiRuntime

ti_destroy_runtime = _taichi_lib.ti_destroy_runtime
ti_destroy_runtime.argtypes = [TiRuntime]
ti_destroy_runtime.restype = None

# Memory
ti_allocate_memory = _taichi_lib.ti_allocate_memory
ti_allocate_memory.argtypes = [TiRuntime, POINTER(TiMemoryAllocateInfo)]
ti_allocate_memory.restype = TiMemory

ti_free_memory = _taichi_lib.ti_free_memory
ti_free_memory.argtypes = [TiRuntime, TiMemory]
ti_free_memory.restype = None

ti_map_memory = _taichi_lib.ti_map_memory
ti_map_memory.argtypes = [TiRuntime, TiMemory]
ti_map_memory.restype = c_void_p

ti_unmap_memory = _taichi_lib.ti_unmap_memory
ti_unmap_memory.argtypes = [TiRuntime, TiMemory]
ti_unmap_memory.restype = None

# Images and Samplers
ti_allocate_image = _taichi_lib.ti_allocate_image
ti_allocate_image.argtypes = [TiRuntime, POINTER(TiImageAllocateInfo)]
ti_allocate_image.restype = TiImage

ti_free_image = _taichi_lib.ti_free_image
ti_free_image.argtypes = [TiRuntime, TiImage]
ti_free_image.restype = None

ti_create_sampler = _taichi_lib.ti_create_sampler
ti_create_sampler.argtypes = [TiRuntime, POINTER(TiSamplerCreateInfo)]
ti_create_sampler.restype = TiSampler

ti_destroy_sampler = _taichi_lib.ti_destroy_sampler
ti_destroy_sampler.argtypes = [TiRuntime, TiSampler]
ti_destroy_sampler.restype = None

# Copy and transition
ti_copy_memory_device_to_device = _taichi_lib.ti_copy_memory_device_to_device
ti_copy_memory_device_to_device.argtypes = [TiRuntime, POINTER(TiMemorySlice), POINTER(TiMemorySlice)]
ti_copy_memory_device_to_device.restype = None

ti_copy_image_device_to_device = _taichi_lib.ti_copy_image_device_to_device
ti_copy_image_device_to_device.argtypes = [TiRuntime, POINTER(TiImageSlice), POINTER(TiImageSlice)]
ti_copy_image_device_to_device.restype = None

ti_track_image_ext = _taichi_lib.ti_track_image_ext
ti_track_image_ext.argtypes = [TiRuntime, TiImage, TiImageLayout]
ti_track_image_ext.restype = None

ti_transition_image = _taichi_lib.ti_transition_image
ti_transition_image.argtypes = [TiRuntime, TiImage, TiImageLayout]
ti_transition_image.restype = None

# Execution
ti_launch_kernel = _taichi_lib.ti_launch_kernel
ti_launch_kernel.argtypes = [TiRuntime, TiKernel, c_uint32, POINTER(TiArgument)]
ti_launch_kernel.restype = None

ti_launch_compute_graph = _taichi_lib.ti_launch_compute_graph
ti_launch_compute_graph.argtypes = [TiRuntime, TiComputeGraph, c_uint32, POINTER(TiNamedArgument)]
ti_launch_compute_graph.restype = None

ti_flush = _taichi_lib.ti_flush
ti_flush.argtypes = [TiRuntime]
ti_flush.restype = None

ti_wait = _taichi_lib.ti_wait
ti_wait.argtypes = [TiRuntime]
ti_wait.restype = None

# AOT module
ti_load_aot_module = _taichi_lib.ti_load_aot_module
ti_load_aot_module.argtypes = [TiRuntime, c_char_p]
ti_load_aot_module.restype = TiAotModule

ti_create_aot_module = _taichi_lib.ti_create_aot_module
ti_create_aot_module.argtypes = [TiRuntime, c_void_p, c_uint64]
ti_create_aot_module.restype = TiAotModule

ti_destroy_aot_module = _taichi_lib.ti_destroy_aot_module
ti_destroy_aot_module.argtypes = [TiAotModule]
ti_destroy_aot_module.restype = None

ti_get_aot_module_kernel = _taichi_lib.ti_get_aot_module_kernel
ti_get_aot_module_kernel.argtypes = [TiAotModule, c_char_p]
ti_get_aot_module_kernel.restype = TiKernel

ti_get_aot_module_compute_graph = _taichi_lib.ti_get_aot_module_compute_graph
ti_get_aot_module_compute_graph.argtypes = [TiAotModule, c_char_p]
ti_get_aot_module_compute_graph.restype = TiComputeGraph
