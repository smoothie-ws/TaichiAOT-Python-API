from ctypes import Structure, POINTER

__all__ = ['TiRuntime',
           'TiAotModule',
           'TiMemory',
           'TiImage',
           'TiKernel',
           'TiComputeGraph',
           'TiSampler']


class _TiRuntime_t(Structure):
    """Taichi runtime represents an instance of a logical backend and its internal dynamic state.
    The user is responsible to synchronize any use of TiRuntime.
    The user must not manipulate multiple TiRuntimes in the same thread."""
    pass


class _TiAotModule_t(Structure):
    """An ahead-of-time (AOT) compiled Taichi module, which contains a collection of kernels and compute graphs."""
    pass


class _TiMemory_t(Structure):
    """A contiguous allocation of device memory."""
    pass


class _TiImage_t(Structure):
    """A contiguous allocation of device image."""
    pass


class _TiKernel_t(Structure):
    """A Taichi kernel that can be launched on the offload target for execution."""
    pass


class _TiComputeGraph_t(Structure):
    """A collection of Taichi kernels (a compute graph) to launch on the offload target in a predefined order."""
    pass


class _TiSampler_t(Structure):
    """An image sampler. Represents a default image sampler provided by the runtime implementation.
     The filter modes and address modes of default samplers depend on backend implementation."""
    pass


TiRuntime = POINTER(_TiRuntime_t)
TiAotModule = POINTER(_TiAotModule_t)
TiMemory = POINTER(_TiMemory_t)
TiImage = POINTER(_TiImage_t)
TiKernel = POINTER(_TiKernel_t)
TiComputeGraph = POINTER(_TiComputeGraph_t)
TiSampler = POINTER(_TiSampler_t)