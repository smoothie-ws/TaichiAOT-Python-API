from ctypes import Structure, POINTER


class _TiRuntime_t(Structure):
    """Description placeholder"""
    pass


class _TiAotModule_t(Structure):
    """Description placeholder"""
    pass


class _TiMemory_t(Structure):
    """Description placeholder"""
    pass


class _TiSampler_t(Structure):
    """Description placeholder"""
    pass


class _TiImage_t(Structure):
    """Description placeholder"""
    pass


class _TiKernel_t(Structure):
    """Description placeholder"""
    pass


class _TiComputeGraph_t(Structure):
    """Description placeholder"""
    pass


TiRuntime = POINTER(_TiRuntime_t)
TiAotModule = POINTER(_TiAotModule_t)
TiMemory = POINTER(_TiMemory_t)
TiSampler = POINTER(_TiSampler_t)
TiImage = POINTER(_TiImage_t)
TiKernel = POINTER(_TiKernel_t)
TiComputeGraph = POINTER(_TiComputeGraph_t)