"""AOT-Taichi-Pybind: Python Bindings for Taichi C-API with Ahead-of-Time
Compilation Support.

This module is designed to seamlessly integrate with Taichi's Ahead-of-Time
(AOT) compilation capabilities, enabling users to leverage the performance
benefits of precompiled Taichi kernels.

Key Features:

- **AOT Compilation Support:** AOT-Taichi-Pybind facilitates the compilation
of Taichi kernels ahead of runtime, optimizing performance by eliminating
the need for just-in-time compilation during execution.

- **Seamless Python Integration:** The module ensures smooth
interoperability between Python and Taichi, allowing users to harness the
power of Taichi's C-API directly from their Python scripts.

- **Efficient Kernel Launching:** Users can launch Taichi kernels with the
provided Python bindings, passing runtime, kernel, and arguments seamlessly.
The module ensures that the provided arguments match the expected count and
types defined in the source code.

- **Enhanced Performance:** By combining Python's flexibility with Taichi's
AOT capabilities, this module aims to provide an efficient and
high-performance interface for working with Taichi, particularly in
scenarios where AOT compilation is advantageous.

"""

from ._functions import *
from ._taichi_c_utils import *

__all__ = [  # aliases
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
    'TiNdShape','TiNdArray', 'TiImageOffset', 'TiImageExtent',
    'TiImageAllocateInfo', 'TiImageSlice','TiSamplerCreateInfo',
    'TiTexture', 'TiScalarValue', 'TiScalar', 'TiTensorValue',
    'TiTensorValueWithLength', 'TiTensor', 'TiArgumentValue',
    'TiArgument', 'TiNamedArgument',

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
    'ti_flush', 'ti_wait']



