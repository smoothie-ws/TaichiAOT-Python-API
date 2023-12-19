"""Python bindings for Taichi C-API."""

from .c_ti_methods import *


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
    'ti_set_runtime_capabilities_ext', 'ti_get_runtime_capabilities',
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