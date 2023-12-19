from ctypes import Union, Structure
from ctypes import (c_uint32, c_uint64, c_float, c_uint8,
                    c_uint16, c_int32, c_char_p)

from .c_ti_aliases import *
from .c_ti_handles import *


class TiCapabilityLevelInfo(Structure):
    """An integral device capability level. It currently is not guaranteed
    that a higher level value is compatible with a lower level value.

    Fields:
        - **capability**: :class:`TiCapability` - `An integral device capability.`
        - **level**: :class:`int` - `The level of the capability.`
    """

    _fields_ = [
        ("capability", c_int),
        ("level", c_uint32)
    ]


class TiMemoryAllocateInfo(Structure):
    """Parameters of a newly allocated memory.

    Fields:
        - **size**: :class:`int` - `Size of the allocation in bytes.`
        - **host_write**: :class:`TiBool` - `True if the host needs to write to the allocated memory.`
        - **host_read**: :class:`TiBool` - `True if the host needs to read from the allocated memory.`
        - **export_sharing**: :class:`TiBool` - `True if the memory allocation needs to be exported to other backends.`
        - **usage**: :class:`TiMemoryUsageFlags` - `All possible usage of this memory allocation.`
    """

    _fields_ = [
        ("size", c_uint64),
        ("host_write", TiBool),
        ("host_read", TiBool),
        ("export_sharing", TiBool),
        ("usage", c_int)
    ]


class TiMemorySlice(Structure):
    """A subsection of a memory allocation.

    Fields:
        - **memory**: :class:`TiMemory` - `The subsectioned memory allocation.`
        - **offset**: :class:`int` - `Offset from the beginning of the allocation.`
        - **size**: :class:`int` - `Size of the subsection.`
    """

    _fields_ = [
        ("memory", TiMemory),
        ("offset", c_uint64),
        ("size", c_uint64)
    ]


class TiNdShape(Structure):
    """Multidimensional size of an ND-array.

    Fields:
        - **dim_count**: :class:`int` - `Number of dimensions.`
        - **dims**: :class:`int` - `Dimension sizes.`
    """

    _fields_ = [
        ("dim_count", c_uint32),
        ("dims", c_uint32 * 16)
    ]


class TiNdArray(Structure):
    """Represents an N-dimensional array.

    Fields:
        - **memory**: :class:`TiMemory` - `Memory bound to the ND-array.`
        - **shape**:  :class:`TiNdShape` - `Shape of the ND-array.`
        - **elem_shape**: :class:`TiNdShape` - `Shape of the ND-array elements.`
        - **elem_type**: :class:`int` - `Primitive data type of the ND-array elements.`
    """

    _fields_ = [
        ("memory", TiMemory),
        ("shape", TiNdShape),
        ("elem_shape", TiNdShape),
        ("elem_type", c_int)
    ]


class TiImageOffset(Structure):
    """Offsets of an image in X, Y, Z, and array layers.

    Fields:
        - **x**: :class:`int` - `Image offset in the X direction.`
        - **y**: :class:`int` - `Image offset in the Y direction. Must be 0 for 1D or 1D array.`
        - **z**: :class:`int` - `Image offset in the Z direction. Must be 0 for 1D, 2D, or cube array.`
        - **array_layer_offset**: :class:`int` - `Image offset in array layers. Must be 0 for 1D, 2D, or 3D array.`
    """

    _fields_ = [
        ("x", c_uint32),
        ("y", c_uint32),
        ("z", c_uint32),
        ("array_layer_offset", c_uint32)
    ]


class TiImageExtent(Structure):
    """Extents of an image in X, Y, Z, and array layers.

    Fields:
        - **width**: :class:`int` - `Image extent in the X direction.`
        - **height**: :class:`int` - `Image extent in the Y direction. Must be 1 for 1D or 1D array.`
        - **depth**: :class:`int` - `Image extent in the Z direction. Must be 1 for 1D, 2D or cube array.`
        - **array_layer_count**: :class:`int` - `Image extent in array layers. Must be 1 for 1D, 2D, or 3D array. Must be 6 for cube array.`
    """

    _fields_ = [
        ("width", c_uint32),
        ("height", c_uint32),
        ("depth", c_uint32),
        ("array_layer_count", c_uint32)
    ]


class TiImageAllocateInfo(Structure):
    """Parameters of a newly allocated image.

    Fields:
        - **dimension**: :class:`TiImageDimension` - `Image dimension.`
        - **extent**: :class:`TiImageExtent` - `Image extent.`
        - **mip_level_count**: :class:`int` - `Number of mip-levels.`
        - **format**: :class:`TiFormat` - `Image texel format.`
        - **export_sharing**: :class:`TiBool` - `True if the memory allocation needs to be exported to other backends (e.g., from Vulkan to CUDA).`
        - **usage**: :class:`TiImageUsageFlags` - `All possible usages of this image allocation. In most cases, TI_IMAGE_USAGE_STORAGE_BIT and TI_IMAGE_USAGE_SAMPLED_BIT enough.`
    """

    _fields_ = [
        ("dimension", c_int),
        ("extent", TiImageExtent),
        ("mip_level_count", c_uint32),
        ("format", c_int),
        ("export_sharing", TiBool),
        ("usage", c_int)
    ]


class TiImageSlice(Structure):
    """Represents a slice of an image.

    Fields:
        - **image**: :class:`TiImage` - `The subsectioned image allocation.`
        - **offset**: :class:`TiImageOffset` - `Offset from the beginning of the allocation in each dimension.`
        - **extent**: :class:`TiImageExtent` - `Size of the subsection in each dimension.`
        - **mip_level**: :class:`int` - `The subsectioned mip-level.`
    """

    _fields_ = [
        ("image", TiImage),
        ("offset", TiImageOffset),
        ("extent", TiImageExtent),
        ("mip_level", c_uint32)
    ]


class TiSamplerCreateInfo(Structure):
    """Parameters for creating a sampler.

    Fields:
        - **mag_filter**: :class:`TiFilter` - `Magnification filter.`
        - **min_filter**: :class:`TiFilter` - `Minification filter.`
        - **address_mode**: :class:`TiAddressMode` - `Address mode.`
        - **max_anisotropy**: :class:`float` - `Maximum anisotropy level.`
    """

    _fields_ = [
        ("mag_filter", c_int),
        ("min_filter", c_int),
        ("address_mode", c_int),
        ("max_anisotropy", c_float)
    ]


class TiTexture(Structure):
    """Image data bound to a sampler.

    Fields:
        - **image**: :class:`TiImage` - `Image bound to the texture.`
        - **sampler**: :class:`TiSampler` - `The bound sampler that controls the sampling behavior of `structure.texture.image`.`
        - **dimension**: :class:`TiImageDimension` - `Image Dimension.`
        - **extent**: :class:`TiImageExtent` - `Image extent.`
        - **format**: :class:`TiFormat` - `Image texel format.`
    """

    _fields_ = [
        ("image", TiImage),
        ("sampler", TiSampler),
        ("dimension", c_int),
        ("extent", TiImageExtent),
        ("format", c_int)
    ]


class TiScalarValue(Union):
    """Scalar value represented by a power-of-two number of bits.

    Fields:
        - **x8**: :class:`int` - `Scalar value that fits into 8 bits.`
        - **x16**: :class:`int` - `Scalar value that fits into 16 bits.`
        - **x32**: :class:`int` - `Scalar value that fits into 32 bits.`
        - **x64**: :class:`int` - `Scalar value that fits into 64 bits.`

    **NOTE:** The unsigned integer types merely hold the number of bits in
    memory and doesn't reflect any type of the underlying data.
    """

    _fields_ = [
        ("x8", c_uint8),
        ("x16", c_uint16),
        ("x32", c_uint32),
        ("x64", c_uint64)
    ]


class TiScalar(Structure):
    """A typed scalar value.

    Fields:
        - **type**: :class:`TiDataType` - `Data type of the scalar.`
        - **value**: :class:`TiScalarValue` - `Value of the scalar.`
    """

    _fields_ = [
        ("type", c_int),
        ("value", TiScalarValue)
    ]


class TiTensorValue(Structure):
    """Tensor value represented by a power-of-two number of bits.

    Fields:
        - **x8**: :class:`int` - `Tensor value that fits into 8 bits.`
        - **x16**: :class:`int` - `Tensor value that fits into 16 bits.`
        - **x32**: :class:`int` - `Tensor value that fits into 32 bits.`
        - **x64**: :class:`int` - `Tensor value that fits into 64 bits.`
    """

    _fields_ = [
        ("x8", c_uint8 * 128),
        ("x16", c_uint16 * 64),
        ("x32", c_uint32 * 32),
        ("x64", c_uint64 * 16)
    ]


class TiTensorValueWithLength(Structure):
    """A tensor value with a length.

    Fields:
        - **length**: :class:`int` - `Length of the tensor.`
        - **data**: :class:`TiTensorValue` - `Data of the tensor.`
    """

    _fields_ = [
        ("length", c_uint32),
        ("data", TiTensorValue)
    ]


class TiTensor(Structure):
    """A typed tensor value.

    Fields:
        - **type**: :class:`TiDataType` - `Data type of the tensor.`
        - **contents**: :class:`TiTensorValueWithLength` - `Contents of the tensor.`
    """

    _fields_ = [
        ("type", c_int),
        ("contents", TiTensorValueWithLength)
    ]


class TiArgumentValue(Union):
    """A scalar or structured argument value.

    Fields:
        - **i32**: :class:`int` - `Value of a 32-bit one's complement signed integer.`
        - **f32**: :class:`float` - `Value of a 32-bit IEEE 754 single-precision floating-point number.`
        - **ndarray**: :class:`TiNdArray` - `An ND-array to be bound.`
        - **texture**: :class:`TiTexture` - `A texture to be bound.`
        - **scalar**: :class:`TiScalar` - `A scalar to be bound.`
        - **tensor**: :class:`TiTensor` - `A tensor to be bound.`
    """

    _fields_ = [
        ("i32", c_int32),
        ("f32", c_float),
        ("ndarray", TiNdArray),
        ("texture", TiTexture),
        ("scalar", TiScalar),
        ("tensor", TiTensor)
    ]


class TiArgument(Structure):
    """An argument value to feed kernels.

    Fields:
        - **type**: :class:`TiArgumentType` - `Type of the argument.`
        - **value**: :class:`TiArgumentValue` - `A Value of the argument.`
    """

    _fields_ = [
        ("type", c_int),
        ("value", TiArgumentValue)
    ]


class TiNamedArgument(Structure):
    """A named argument value to feed compute graphs.

    Fields:
        - **name**: :class:`str` - `Name of the argument.`
        - **argument**: :class:`TiArgument` - `Argument body.`
    """

    _fields_ = [
        ("name", c_char_p),
        ("argument", TiArgument)
    ]
