from ctypes import c_void_p, POINTER

from .c_ti_enums import *
from .c_ti_structs import *

TAICHI_C_API_METHODS = {
    'ti_get_version': {
        'restype': c_uint32
    },
    'ti_get_available_archs': {
        'restype': None
    },
    'ti_get_last_error': {
        'argtypes': [POINTER(c_uint64), c_char_p],
        'restype': TiError
    },
    'ti_set_last_error': {
        'argtypes': [c_uint32, c_char_p],
        'restype': None
    },
    'ti_create_runtime': {
        'argtypes': [c_int, c_uint32],
        'restype': TiRuntime
    },
    'ti_destroy_runtime': {
        'argtypes': [TiRuntime],
        'restype': None
    },
    'ti_set_runtime_capabilities_ext': {
        'argtypes': [TiRuntime, c_uint32, POINTER(TiCapabilityLevelInfo)],
        'restype': None
    },
    'ti_get_runtime_capabilities': {
        'argtypes': [TiRuntime, c_uint32, POINTER(TiCapabilityLevelInfo)],
        'restype': None
    },
    'ti_allocate_memory': {
        'argtypes': [TiRuntime, POINTER(TiMemoryAllocateInfo)],
        'restype': TiMemory
    },
    'ti_free_memory': {
        'argtypes': [TiRuntime, TiMemory],
        'restype': None
    },
    'ti_map_memory': {
        'argtypes': [TiRuntime, TiMemory],
        'restype': c_void_p
    },
    'ti_unmap_memory': {
        'argtypes': [TiRuntime, TiMemory],
        'restype': None
    },
    'ti_allocate_image': {
        'argtypes': [TiRuntime, POINTER(TiImageAllocateInfo)],
        'restype': TiImage
    },
    'ti_free_image': {
        'argtypes': [TiRuntime, TiImage],
        'restype': None
    },
    'ti_create_sampler': {
        'argtypes': [TiRuntime, POINTER(TiSamplerCreateInfo)],
        'restype': TiSampler
    },
    'ti_destroy_sampler': {
        'argtypes': [TiRuntime, TiSampler],
        'restype': None
    },
    'ti_copy_memory_device_to_device': {
        'argtypes': [TiRuntime, POINTER(TiMemorySlice),
                     POINTER(TiMemorySlice)],
        'restype': None
    },
    'ti_copy_image_device_to_device': {
        'argtypes': [TiRuntime, POINTER(TiImageSlice), POINTER(TiImageSlice)],
        'restype': None
    },
    'ti_track_image_ext': {
        'argtypes': [TiRuntime, TiImage, c_int],
        'restype': None
    },
    'ti_transition_image': {
        'argtypes': [TiRuntime, TiImage, c_int],
        'restype': None
    },
    'ti_launch_kernel': {
        'argtypes': [TiRuntime, TiKernel, c_uint32, POINTER(TiArgument)],
        'restype': None
    },
    'ti_launch_compute_graph': {
        'argtypes': [TiRuntime, TiComputeGraph, c_uint32, c_void_p],
        'restype': None
    },
    'ti_flush': {
        'argtypes': [TiRuntime],
        'restype': None
    },
    'ti_wait': {
        'argtypes': [TiRuntime],
        'restype': None
    },
    'ti_load_aot_module': {
        'argtypes': [TiRuntime, c_char_p],
        'restype': TiAotModule
    },
    'ti_create_aot_module': {
        'argtypes': [TiRuntime, c_void_p, c_uint64],
        'restype': TiAotModule
    },
    'ti_destroy_aot_module': {
        'argtypes': [TiAotModule],
        'restype': None
    },
    'ti_get_aot_module_kernel': {
        'argtypes': [TiAotModule, c_char_p],
        'restype': TiKernel
    },
    'ti_get_aot_module_compute_graph': {
        'argtypes': [TiAotModule, c_char_p],
        'restype': TiComputeGraph
    },
}