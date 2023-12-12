from ctypes import Structure, c_uint32, c_uint64, c_bool, c_float, c_uint8, Union, c_uint16, c_int32, c_char_p, POINTER

from .TiAliases import TiBool
from .TiHandles import TiMemory, TiImage, TiSampler


class TiCapabilityLevelInfo(Structure):
    """Description placeholder"""

    _fields_ = [
        ("capability", c_uint32),
        ("level", c_uint32)
    ]


class TiMemoryAllocateInfo(Structure):
    """Parameters of a newly allocated memory."""

    _fields_ = [
        ("size", c_uint64),  # Size of the allocation in bytes.
        ("host_write", TiBool),  # True if the host needs to write to the allocated memory.
        ("host_read", TiBool),  # True if the host needs to read from the allocated memory.
        ("export_sharing", TiBool),  # True if the memory allocation needs to be exported to other backends
        ("usage", c_uint32)  # All possible usage of this memory allocation.
    ]


class TiMemorySlice(Structure):
    """Description placeholder"""

    _fields_ = [
        ("memory", TiMemory),
        ("offset", c_uint64),
        ("size", c_uint64)
    ]


class TiNdShape(Structure):
    """Description placeholder"""

    _fields_ = [
        ("dim_count", c_uint32),
        ("dims", c_uint32 * 16)
    ]


class TiNdArray(Structure):
    """Description placeholder"""

    _fields_ = [
        ("memory", TiMemory),
        ("shape", TiNdShape),
        ("elem_shape", TiNdShape),
        ("elem_type", c_uint32)
    ]


class TiImageOffset(Structure):
    """Description placeholder"""

    _fields_ = [
        ("array_layer_offset", c_uint32)
    ]


class TiImageExtent(Structure):
    """Description placeholder"""

    _fields_ = [
        ("width", c_uint32),
        ("height", c_uint32),
        ("depth", c_uint32),
        ("array_layer_count", c_uint32)
    ]


class TiImageAllocateInfo(Structure):
    """Description placeholder"""

    _fields_ = [
        ("dimension", c_uint32),
        ("extent", TiImageExtent),
        ("mip_level_count", c_uint32),
        ("format", c_uint32),
        ("export_sharing", c_bool),
        ("usage", c_uint32)
    ]


class TiImageSlice(Structure):
    """Description placeholder"""

    _fields_ = [
        ("image", TiImage),
        ("offset", TiImageOffset),
        ("extent", TiImageExtent),
        ("mip_level", c_uint32)
    ]


class TiSamplerCreateInfo(Structure):
    """Description placeholder"""

    _fields_ = [
        ("mag_filter", c_uint32),
        ("min_filter", c_uint32),
        ("address_mode", c_uint32),
        ("max_anisotropy", c_float)
    ]


class TiTexture(Structure):
    """Description placeholder"""

    _fields_ = [
        ("image", TiImage),
        ("sampler", TiSampler),
        ("dimension", c_uint32),
        ("extent", TiImageExtent),
        ("format", c_uint32)
    ]


class TiScalarValue(Union):
    """Description placeholder"""

    _fields_ = [
        ("x8", c_uint8),
        ("x16", c_uint16),
        ("x32", c_uint32),
        ("x64", c_uint64)
    ]


class TiScalar(Structure):
    """Description placeholder"""

    _fields_ = [
        ("type", c_uint32),
        ("value", TiScalarValue)
    ]


class TiTensorValue(Structure):
    """Description placeholder"""

    _fields_ = [
        ("x8", c_uint8 * 128),
        ("x16", c_uint16 * 64),
        ("x32", c_uint32 * 32),
        ("x64", c_uint64 * 16)
    ]


class TiTensorValueWithLength(Structure):
    """Description placeholder"""

    _fields_ = [
        ("length", c_uint32),
        ("data", TiTensorValue)
    ]


class TiTensor(Structure):
    """Description placeholder"""

    _fields_ = [
        ("type", c_uint32),
        ("contents", TiTensorValueWithLength)
    ]


class TiArgumentValue(Union):
    """A scalar or structured argument value."""

    _fields_ = [
        ("i32", c_int32),
        ("f32", c_float),
        ("ndarray", TiNdArray),
        ("texture", TiTexture),
        ("scalar", TiScalar),
        ("tensor", TiTensor)
    ]


class TiArgument(Structure):
    """Description placeholder"""

    _fields_ = [("type", c_uint32),
                ("value", TiArgumentValue)
                ]


class TiNamedArgument(Structure):
    """Description placeholder"""

    _fields_ = [
        ("name", c_char_p),
        ("argument", TiArgument)
    ]