from ctypes import CDLL, c_void_p

from .taichi_c_utils import *
from os.path import dirname, join, abspath

__all__ = ['c_ti_get_version',
           'c_ti_get_last_error',
           'c_ti_set_last_error',
           'c_ti_create_runtime',
           'c_ti_allocate_memory',
           'c_ti_free_memory',
           'c_ti_map_memory',
           'c_ti_unmap_memory',
           'c_ti_get_available_archs',
           'c_ti_destroy_runtime',
           'c_ti_allocate_image',
           'c_ti_free_image',
           'c_ti_create_sampler',
           'c_ti_destroy_sampler',
           'c_ti_copy_memory_device_to_device',
           'c_ti_copy_image_device_to_device',
           'c_ti_track_image_ext',
           'c_ti_transition_image',
           'c_ti_launch_kernel',
           'c_ti_launch_compute_graph',
           'c_ti_flush',
           'c_ti_wait',
           'c_ti_load_aot_module',
           'c_ti_create_aot_module',
           'c_ti_destroy_aot_module',
           'c_ti_get_aot_module_kernel',
           'c_ti_get_aot_module_compute_graph']

_current_folder = dirname(abspath(__file__))
_taichi_lib_path = join(_current_folder, 'taichi_c_api.dll')
_taichi_lib = CDLL(_taichi_lib_path)

c_ti_get_version = _taichi_lib.ti_get_version
c_ti_get_version.argtypes = None
c_ti_get_version.restype = c_uint32

c_ti_get_available_archs = _taichi_lib.ti_get_available_archs
c_ti_get_available_archs.argtypes = None
c_ti_get_available_archs.restype = None

c_ti_get_last_error = _taichi_lib.ti_get_last_error
c_ti_get_last_error.argtypes = [POINTER(c_uint64), c_char_p]
c_ti_get_last_error.restype = TiError

c_ti_set_last_error = _taichi_lib.ti_set_last_error
c_ti_set_last_error.argtypes = [c_uint32, c_char_p]
c_ti_set_last_error.restype = None

c_ti_create_runtime = _taichi_lib.ti_create_runtime
c_ti_create_runtime.argtypes = [c_int, c_uint32]
c_ti_create_runtime.restype = TiRuntime

c_ti_destroy_runtime = _taichi_lib.ti_destroy_runtime
c_ti_destroy_runtime.argtypes = [TiRuntime]
c_ti_destroy_runtime.restype = None

c_ti_allocate_memory = _taichi_lib.ti_allocate_memory
c_ti_allocate_memory.argtypes = [TiRuntime, POINTER(TiMemoryAllocateInfo)]
c_ti_allocate_memory.restype = TiMemory

c_ti_free_memory = _taichi_lib.ti_free_memory
c_ti_free_memory.argtypes = [TiRuntime, TiMemory]
c_ti_free_memory.restype = None

c_ti_map_memory = _taichi_lib.ti_map_memory
c_ti_map_memory.argtypes = [TiRuntime, TiMemory]
c_ti_map_memory.restype = c_void_p

c_ti_unmap_memory = _taichi_lib.ti_unmap_memory
c_ti_unmap_memory.argtypes = [TiRuntime, TiMemory]
c_ti_unmap_memory.restype = None

c_ti_allocate_image = _taichi_lib.ti_allocate_image
c_ti_allocate_image.argtypes = [TiRuntime, POINTER(TiImageAllocateInfo)]
c_ti_allocate_image.restype = TiImage

c_ti_free_image = _taichi_lib.ti_free_image
c_ti_free_image.argtypes = [TiRuntime, TiImage]
c_ti_free_image.restype = None

c_ti_create_sampler = _taichi_lib.ti_create_sampler
c_ti_create_sampler.argtypes = [TiRuntime, POINTER(TiSamplerCreateInfo)]
c_ti_create_sampler.restype = TiSampler

c_ti_destroy_sampler = _taichi_lib.ti_destroy_sampler
c_ti_destroy_sampler.argtypes = [TiRuntime, TiSampler]
c_ti_destroy_sampler.restype = None

c_ti_copy_memory_device_to_device = _taichi_lib.ti_copy_memory_device_to_device
c_ti_copy_memory_device_to_device.argtypes = [TiRuntime, POINTER(TiMemorySlice), POINTER(TiMemorySlice)]
c_ti_copy_memory_device_to_device.restype = None

c_ti_copy_image_device_to_device = _taichi_lib.ti_copy_image_device_to_device
c_ti_copy_image_device_to_device.argtypes = [TiRuntime, POINTER(TiImageSlice), POINTER(TiImageSlice)]
c_ti_copy_image_device_to_device.restype = None

c_ti_track_image_ext = _taichi_lib.ti_track_image_ext
c_ti_track_image_ext.argtypes = [TiRuntime, TiImage, c_int]
c_ti_track_image_ext.restype = None

c_ti_transition_image = _taichi_lib.ti_transition_image
c_ti_transition_image.argtypes = [TiRuntime, TiImage, c_int]
c_ti_transition_image.restype = None

c_ti_launch_kernel = _taichi_lib.ti_launch_kernel
c_ti_launch_kernel.argtypes = [TiRuntime, TiKernel, c_uint32, POINTER(TiArgument)]
c_ti_launch_kernel.restype = None

c_ti_launch_compute_graph = _taichi_lib.ti_launch_compute_graph
c_ti_launch_compute_graph.argtypes = [TiRuntime, TiComputeGraph, c_uint32, c_void_p]
c_ti_launch_compute_graph.restype = None

c_ti_flush = _taichi_lib.ti_flush
c_ti_flush.argtypes = [TiRuntime]
c_ti_flush.restype = None

c_ti_wait = _taichi_lib.ti_wait
c_ti_wait.argtypes = [TiRuntime]
c_ti_wait.restype = None

c_ti_load_aot_module = _taichi_lib.ti_load_aot_module
c_ti_load_aot_module.argtypes = [TiRuntime, c_char_p]
c_ti_load_aot_module.restype = TiAotModule

c_ti_create_aot_module = _taichi_lib.ti_create_aot_module
c_ti_create_aot_module.argtypes = [TiRuntime, c_void_p, c_uint64]
c_ti_create_aot_module.restype = TiAotModule

c_ti_destroy_aot_module = _taichi_lib.ti_destroy_aot_module
c_ti_destroy_aot_module.argtypes = [TiAotModule]
c_ti_destroy_aot_module.restype = None

c_ti_get_aot_module_kernel = _taichi_lib.ti_get_aot_module_kernel
c_ti_get_aot_module_kernel.argtypes = [TiAotModule, c_char_p]
c_ti_get_aot_module_kernel.restype = TiKernel

c_ti_get_aot_module_compute_graph = _taichi_lib.ti_get_aot_module_compute_graph
c_ti_get_aot_module_compute_graph.argtypes = [TiAotModule, c_char_p]
c_ti_get_aot_module_compute_graph.restype = TiComputeGraph
