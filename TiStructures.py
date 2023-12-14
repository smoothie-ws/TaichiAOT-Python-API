"""Module providing ctypes structures for TiRuntime."""

from ctypes import Structure, c_uint32, c_uint64, c_float, c_uint8, Union, c_uint16, c_int32, c_char_p

from .TiAliases import TiBool
from .TiEnumerations import *
from .TiHandles import TiMemory, TiImage, TiSampler


class CapabilityLevelInfo(Structure):
    """An integral device capability level.
    It currently is not guaranteed that a higher level value is compatible with a lower level value."""

    _fields_ = [
        ("capability", TiCapability),
        ("level", c_uint32)
    ]


class TiMemoryAllocateInfo(Structure):
    """Parameters of a newly allocated memory."""
    _fields_ = [
        ("size", c_uint64),  # Size of the allocation in bytes.
        ("host_write", TiBool),  # True if the host needs to write to the allocated memory.
        ("host_read", TiBool),  # True if the host needs to read from the allocated memory.
        ("export_sharing", TiBool),  # True if the memory allocation needs to be exported to other backends.
        ("usage", TiMemoryUsageFlags)  # All possible usage of this memory allocation.
    ]


class TiMemorySlice(Structure):
    """A subsection of a memory allocation."""

    _fields_ = [
        ("memory", TiMemory),  # The subsectioned memory allocation.
        ("offset", c_uint64),  # Offset from the beginning of the allocation.
        ("size", c_uint64)  # Size of the subsection.
    ]


class TiNdShape(Structure):
    """Multi-dimensional size of an ND-array."""

    _fields_ = [
        ("dim_count", c_uint32),  # Number of dimensions.
        ("dims", c_uint32 * 16)  # Dimension sizes.
    ]


class TiNdArray(Structure):
    """Represents an N-dimensional array."""

    _fields_ = [
        ("memory", TiMemory),  # Memory bound to the ND-array.
        ("shape", TiNdShape),  # Shape of the ND-array.
        ("elem_shape", TiNdShape),  # Shape of the ND-array elements.
        ("elem_type", TiDataType)  # Primitive data type of the ND-array elements.
    ]


class TiImageOffset(Structure):
    """Offsets of an image in X, Y, Z, and array layers."""

    _fields_ = [
        ("x", c_uint32),  # Image offset in the X direction.
        ("y", c_uint32),  # Image offset in the Y direction. Must be 0 for 1D or 1D array.
        ("z", c_uint32),  # Image offset in the Z direction. Must be 0 for 1D, 2D, or cube array.
        ("array_layer_offset", c_uint32)  # Image offset in array layers. Must be 0 for 1D, 2D, or 3D array.
    ]


class TiImageExtent(Structure):
    """Extents of an image in X, Y, Z, and array layers."""

    _fields_ = [
        ("width", c_uint32),  # Image extent in the X direction.
        ("height", c_uint32),  # Image extent in the Y direction. Must be 1 for 1D or 1D array.
        ("depth", c_uint32),  # Image extent in the Z direction. Must be 1 for 1D, 2D or cube array.
        ("array_layer_count", c_uint32)
        # Image extent in array layers. Must be 1 for 1D, 2D, or 3D array. Must be 6 for cube array.
    ]


class TiImageAllocateInfo(Structure):
    """Parameters of a newly allocated image."""

    _fields_ = [
        ("dimension", TiImageDimension),  # Image dimension.
        ("extent", TiImageExtent),  # Image extent.
        ("mip_level_count", c_uint32),  # Number of mip-levels.
        ("format", TiFormat),  # Image texel format.
        ("export_sharing", TiBool),  # True if the memory allocation needs to be exported to other backends.
        ("usage", TiImageUsageFlags)  # All possible usages of this image allocation.
    ]


class TiImageSlice(Structure):
    """Represents a slice of an image."""

    _fields_ = [
        ("image", TiImage),  # The subsectioned image allocation.
        ("offset", TiImageOffset),  # Offset from the beginning of the allocation in each dimension.
        ("extent", TiImageExtent),  # Size of the subsection in each dimension.
        ("mip_level", c_uint32)  # The subsectioned mip-level.
    ]


class TiSamplerCreateInfo(Structure):
    """Parameters for creating a sampler."""

    _fields_ = [
        ("mag_filter", TiFilter),  # Magnification filter.
        ("min_filter", TiFilter),  # Minification filter.
        ("address_mode", TiAddressMode),  # Address mode.
        ("max_anisotropy", c_float)  # Maximum anisotropy level.
    ]


class TiTexture(Structure):
    """Image data bound to a sampler."""

    _fields_ = [
        ("image", TiImage),  # Image bound to the texture.
        ("sampler", TiSampler),  # The bound sampler that controls the sampling behavior of `structure.texture.image`.
        ("dimension", TiImageDimension),  # Image Dimension.
        ("extent", TiImageExtent),  # Image extent.
        ("format", TiFormat)  # Image texel format.
    ]


class TiScalarValue(Union):
    """Scalar value represented by a power-of-two number of bits."""
    """NOTE:
        The unsigned integer types merely hold the number of bits in memory
        and doesn't reflect any type of the underlying data. For example, a 32-bit
        floating-point scalar value is assigned by `*(float*)&scalar_value.x32 =
        0.0f`; a 16-bit signed integer is assigned by `*(int16_t)&scalar_vaue.x16 =
        1`. The actual type of the scalar is hinted via `type`."""

    _fields_ = [
        ("x8", c_uint8),  # Scalar value that fits into 8 bits.
        ("x16", c_uint16),  # Scalar value that fits into 16 bits.
        ("x32", c_uint32),  # Scalar value that fits into 32 bits.
        ("x64", c_uint64)  # Scalar value that fits into 64 bits.
    ]


class TiScalar(Structure):
    """A typed scalar value."""

    _fields_ = [
        ("type", TiDataType),  # Data type of the scalar.
        ("value", TiScalarValue)  # Value of the scalar.
    ]


class TiTensorValue(Structure):
    """Tensor value represented by a power-of-two number of bits."""

    _fields_ = [
        ("x8", c_uint8 * 128),  # Tensor value that fits into 8 bits.
        ("x16", c_uint16 * 64),  # Tensor value that fits into 16 bits.
        ("x32", c_uint32 * 32),  # Tensor value that fits into 32 bits.
        ("x64", c_uint64 * 16)  # Tensor value that fits into 64 bits.
    ]


class TiTensorValueWithLength(Structure):
    """A tensor value with a length."""

    _fields_ = [
        ("length", c_uint32),  # Length of the tensor.
        ("data", TiTensorValue)  # Data of the tensor.
    ]


class TiTensor(Structure):
    """A typed tensor value."""

    _fields_ = [
        ("type", TiDataType),  # Data type of the tensor.
        ("contents", TiTensorValueWithLength)  # Contents of the tensor.
    ]


class TiArgumentValue(Union):
    """A scalar or structured argument value."""

    _fields_ = [
        ("i32", c_int32),  # Value of a 32-bit one's complement signed integer.
        ("f32", c_float),  # Value of a 32-bit IEEE 754 single-precision floating-poing number.
        ("ndarray", TiNdArray),  # An ND-array to be bound.
        ("texture", TiTexture),  # A texture to be bound.
        ("scalar", TiScalar),  # A scalar to be bound.
        ("tensor", TiTensor)  # A tensor to be bound.
    ]


class TiArgument(Structure):
    """An argument value to feed kernels."""

    _fields_ = [
        ("type", TiArgumentType),  # Type of the argument.
        ("value", TiArgumentValue)  # A Value of the argument.
    ]


class TiNamedArgument(Structure):
    """A named argument value to feed compute graphs."""

    _fields_ = [
        ("name", c_char_p),  # Name of the argument.
        ("argument", TiArgument)  # Argument body.
    ]
