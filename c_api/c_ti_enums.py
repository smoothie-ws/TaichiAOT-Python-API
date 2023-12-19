from enum import IntEnum


class _TiMemoryUsageFlagBits(IntEnum):
    TI_MEMORY_USAGE_STORAGE_BIT = 1 << 0
    TI_MEMORY_USAGE_UNIFORM_BIT = 1 << 1
    TI_MEMORY_USAGE_VERTEX_BIT = 1 << 2
    TI_MEMORY_USAGE_INDEX_BIT = 1 << 3


class _TiImageUsageFlagBits(IntEnum):
    TI_IMAGE_USAGE_STORAGE_BIT = 1 << 0
    TI_IMAGE_USAGE_SAMPLED_BIT = 1 << 1
    TI_IMAGE_USAGE_ATTACHMENT_BIT = 1 << 2


class TiError(IntEnum):
    """Errors reported by Taichi C-API.

    - **TI_ERROR_SUCCESS**: The Taichi C-API invocation finished gracefully.
    - **TI_ERROR_NOT_SUPPORTED**: Unsupported combination.
    - **TI_ERROR_CORRUPTED_DATA**: Corrupted data.
    - **TI_ERROR_NAME_NOT_FOUND**: Name not found.
    - **TI_ERROR_INVALID_ARGUMENT**: Invalid argument or mismatch.
    - **TI_ERROR_ARGUMENT_NULL**: Argument points to null.
    - **TI_ERROR_ARGUMENT_OUT_OF_RANGE**: Argument out of range.
    - **TI_ERROR_ARGUMENT_NOT_FOUND**: Kernel argument missing.
    - **TI_ERROR_INVALID_INTEROP**: Invalid interoperation.
    - **TI_ERROR_INVALID_STATE**: Unrecoverable invalid state.
    - **TI_ERROR_INCOMPATIBLE_MODULE**: Module is incompatible.
    - **TI_ERROR_OUT_OF_MEMORY**: Out of memory.
    """

    TI_ERROR_SUCCESS = 0
    TI_ERROR_NOT_SUPPORTED = -1
    TI_ERROR_CORRUPTED_DATA = -2
    TI_ERROR_NAME_NOT_FOUND = -3
    TI_ERROR_INVALID_ARGUMENT = -4
    TI_ERROR_ARGUMENT_NULL = -5
    TI_ERROR_ARGUMENT_OUT_OF_RANGE = -6
    TI_ERROR_ARGUMENT_NOT_FOUND = -7
    TI_ERROR_INVALID_INTEROP = -8
    TI_ERROR_INVALID_STATE = -9
    TI_ERROR_INCOMPATIBLE_MODULE = -10
    TI_ERROR_OUT_OF_MEMORY = -11
    TI_ERROR_MAX_ENUM = 0xffffffff

    @classmethod
    def get_error_details(cls, error_code: int) -> str:
        """Get the error details for a given error code."""

        error_messages = {
            cls.TI_ERROR_SUCCESS.value: "The Taichi C-API invocation finished gracefully.",
            cls.TI_ERROR_NOT_SUPPORTED.value: "The invoked API, or the combination of parameters is not supported by the Taichi C-API.",
            cls.TI_ERROR_CORRUPTED_DATA.value: "Provided data is corrupted.",
            cls.TI_ERROR_NAME_NOT_FOUND.value: "Provided name does not refer to any existing item.",
            cls.TI_ERROR_INVALID_ARGUMENT.value: "One or more function arguments violate constraints specified in C-API documents, or kernel arguments mismatch the kernel argument list defined in the AOT module.",
            cls.TI_ERROR_ARGUMENT_NULL.value: "One or more by-reference (pointer) function arguments point to null.",
            cls.TI_ERROR_ARGUMENT_OUT_OF_RANGE.value: "One or more function arguments are out of its acceptable range; or enumeration arguments have undefined value.",
            cls.TI_ERROR_ARGUMENT_NOT_FOUND.value: "One or more kernel arguments are missing.",
            cls.TI_ERROR_INVALID_INTEROP.value: "The intended interoperation is not possible on the current arch. For example, attempts to export a Vulkan object from a CUDA runtime are not allowed.",
            cls.TI_ERROR_INVALID_STATE.value: "The Taichi C-API enters an unrecoverable invalid state. Related Taichi objects are potentially corrupted. The users should release the contaminated resources for stability. Please feel free to file an issue if you encountered this error in a normal routine.",
            cls.TI_ERROR_INCOMPATIBLE_MODULE.value: "The AOT module is not compatible with the current runtime.",
            cls.TI_ERROR_OUT_OF_MEMORY.value: "Out of memory.",
            cls.TI_ERROR_MAX_ENUM.value: "Maximum value of the enumeration."
        }

        return error_messages.get(error_code,
                                  f"Unknown error code: {error_code}")


class TiArch(IntEnum):
    """Types of backend architectures.

    - **TI_ARCH_VULKAN**: Vulkan GPU backend.
    - **TI_ARCH_METAL**: Metal GPU backend.
    - **TI_ARCH_CUDA**: NVIDIA CUDA GPU backend.
    - **TI_ARCH_X64**: x64 native CPU backend.
    - **TI_ARCH_ARM64**: Arm64 native CPU backend.
    - **TI_ARCH_OPENGL**: OpenGL GPU backend.
    - **TI_ARCH_GLES**: OpenGL ES GPU backend.
    """

    TI_ARCH_RESERVED = 0
    TI_ARCH_VULKAN = 1
    TI_ARCH_METAL = 2
    TI_ARCH_CUDA = 3
    TI_ARCH_X64 = 4
    TI_ARCH_ARM64 = 5
    TI_ARCH_OPENGL = 6
    TI_ARCH_GLES = 7
    TI_ARCH_MAX_ENUM = 0xffffffff


class TiCapability(IntEnum):
    """Device capabilities.

    - **TI_CAPABILITY_SPIRV_VERSION**: *SPIR-V version* capability.
    - **TI_CAPABILITY_SPIRV_HAS_INT8**: supports int8.
    - **TI_CAPABILITY_SPIRV_HAS_INT16**: supports int16.
    - **TI_CAPABILITY_SPIRV_HAS_INT64**: supports int64.
    - **TI_CAPABILITY_SPIRV_HAS_FLOAT16**: supports float16.
    - **TI_CAPABILITY_SPIRV_HAS_FLOAT64**: supports float64.
    - **TI_CAPABILITY_SPIRV_HAS_ATOMIC_INT64**: atomic operations on int64.
    - **TI_CAPABILITY_SPIRV_HAS_ATOMIC_FLOAT16**: atomic operations on float16.
    - **TI_CAPABILITY_SPIRV_HAS_ATOMIC_FLOAT16_ADD**: atomic add on float16.
    - **TI_CAPABILITY_SPIRV_HAS_ATOMIC_FLOAT16_MINMAX**: atomic min/max on float16.
    - **TI_CAPABILITY_SPIRV_HAS_ATOMIC_FLOAT**: atomic operations on float.
    - **TI_CAPABILITY_SPIRV_HAS_ATOMIC_FLOAT_ADD**: atomic add on float.
    - **TI_CAPABILITY_SPIRV_HAS_ATOMIC_FLOAT_MINMAX**: atomic min/max on float.
    - **TI_CAPABILITY_SPIRV_HAS_ATOMIC_FLOAT64**: atomic operations on float64.
    - **TI_CAPABILITY_SPIRV_HAS_ATOMIC_FLOAT64_ADD**: atomic add on float64.
    - **TI_CAPABILITY_SPIRV_HAS_ATOMIC_FLOAT64_MINMAX**: atomic min/max on float64.
    - **TI_CAPABILITY_SPIRV_HAS_VARIABLE_PTR**: variable pointer.
    - **TI_CAPABILITY_SPIRV_HAS_PHYSICAL_STORAGE_BUFFER**: physical storage buffer.
    - **TI_CAPABILITY_SPIRV_HAS_SUBGROUP_BASIC**: basic subgroup operations.
    - **TI_CAPABILITY_SPIRV_HAS_SUBGROUP_VOTE**: subgroup vote operations.
    - **TI_CAPABILITY_SPIRV_HAS_SUBGROUP_ARITHMETIC**: subgroup arithmetic operations.
    - **TI_CAPABILITY_SPIRV_HAS_SUBGROUP_BALLOT**: subgroup ballot operations.
    - **TI_CAPABILITY_SPIRV_HAS_NON_SEMANTIC_INFO**: non-semantic information.
    - **TI_CAPABILITY_SPIRV_HAS_NO_INTEGER_WRAP_DECORATION**: no integer wrap decoration.
    """

    TI_CAPABILITY_RESERVED = 0
    TI_CAPABILITY_SPIRV_VERSION = 1
    TI_CAPABILITY_SPIRV_HAS_INT8 = 2
    TI_CAPABILITY_SPIRV_HAS_INT16 = 3
    TI_CAPABILITY_SPIRV_HAS_INT64 = 4
    TI_CAPABILITY_SPIRV_HAS_FLOAT16 = 5
    TI_CAPABILITY_SPIRV_HAS_FLOAT64 = 6
    TI_CAPABILITY_SPIRV_HAS_ATOMIC_INT64 = 7
    TI_CAPABILITY_SPIRV_HAS_ATOMIC_FLOAT16 = 8
    TI_CAPABILITY_SPIRV_HAS_ATOMIC_FLOAT16_ADD = 9
    TI_CAPABILITY_SPIRV_HAS_ATOMIC_FLOAT16_MINMAX = 10
    TI_CAPABILITY_SPIRV_HAS_ATOMIC_FLOAT = 11
    TI_CAPABILITY_SPIRV_HAS_ATOMIC_FLOAT_ADD = 12
    TI_CAPABILITY_SPIRV_HAS_ATOMIC_FLOAT_MINMAX = 13
    TI_CAPABILITY_SPIRV_HAS_ATOMIC_FLOAT64 = 14
    TI_CAPABILITY_SPIRV_HAS_ATOMIC_FLOAT64_ADD = 15
    TI_CAPABILITY_SPIRV_HAS_ATOMIC_FLOAT64_MINMAX = 16
    TI_CAPABILITY_SPIRV_HAS_VARIABLE_PTR = 17
    TI_CAPABILITY_SPIRV_HAS_PHYSICAL_STORAGE_BUFFER = 18
    TI_CAPABILITY_SPIRV_HAS_SUBGROUP_BASIC = 19
    TI_CAPABILITY_SPIRV_HAS_SUBGROUP_VOTE = 20
    TI_CAPABILITY_SPIRV_HAS_SUBGROUP_ARITHMETIC = 21
    TI_CAPABILITY_SPIRV_HAS_SUBGROUP_BALLOT = 22
    TI_CAPABILITY_SPIRV_HAS_NON_SEMANTIC_INFO = 23
    TI_CAPABILITY_SPIRV_HAS_NO_INTEGER_WRAP_DECORATION = 24
    TI_CAPABILITY_MAX_ENUM = 0xffffffff


class TiDataType(IntEnum):
    """Elementary data types.

     There might be vendor-specific constraints on the available data types,
    so it's recommended to use 32-bit data types if multi-platform
    distribution is desired.

    - **TI_DATA_TYPE_F16**: 16-bit half-precision floating-point number.
    - **TI_DATA_TYPE_F32**: 32-bit single-precision floating-point number.
    - **TI_DATA_TYPE_F64**: 64-bit double-precision floating-point number.
    - **TI_DATA_TYPE_I8**: 8-bit one's complement signed integer.
    - **TI_DATA_TYPE_I16**: 16-bit one's complement signed integer.
    - **TI_DATA_TYPE_I32**: 32-bit one's complement signed integer.
    - **TI_DATA_TYPE_I64**: 64-bit one's complement signed integer.
    - **TI_DATA_TYPE_U1**: 1-bit unsigned integer.
    - **TI_DATA_TYPE_U8**: 8-bit unsigned integer.
    - **TI_DATA_TYPE_U16**: 16-bit unsigned integer.
    - **TI_DATA_TYPE_U32**: 32-bit unsigned integer.
    - **TI_DATA_TYPE_U64**: 64-bit unsigned integer.
    - **TI_DATA_TYPE_GEN**: Generic data type.
    - **TI_DATA_TYPE_UNKNOWN**: Unknown data type.
    """

    TI_DATA_TYPE_F16 = 0
    TI_DATA_TYPE_F32 = 1
    TI_DATA_TYPE_F64 = 2
    TI_DATA_TYPE_I8 = 3
    TI_DATA_TYPE_I16 = 4
    TI_DATA_TYPE_I32 = 5
    TI_DATA_TYPE_I64 = 6
    TI_DATA_TYPE_U1 = 7
    TI_DATA_TYPE_U8 = 8
    TI_DATA_TYPE_U16 = 9
    TI_DATA_TYPE_U32 = 10
    TI_DATA_TYPE_U64 = 11
    TI_DATA_TYPE_GEN = 12
    TI_DATA_TYPE_UNKNOWN = 13
    TI_DATA_TYPE_MAX_ENUM = 4294967295


class TiArgumentType(IntEnum):
    """Types of kernel and compute graph arguments.

    - **TI_ARGUMENT_TYPE_I32**: 32-bit one's complement signed integer.
    - **TI_ARGUMENT_TYPE_F32**: 32-bit IEEE 754 single-precision floating-point number.
    - **TI_ARGUMENT_TYPE_NDARRAY**: ND-array wrapped around a :class:`TiMemory`.
    - **TI_ARGUMENT_TYPE_TEXTURE**: Texture wrapped around a :class:`TiImage`.
    - **TI_ARGUMENT_TYPE_SCALAR**: Typed scalar.
    - **TI_ARGUMENT_TYPE_TENSOR**: Typed tensor.
    """

    TI_ARGUMENT_TYPE_I32 = 0
    TI_ARGUMENT_TYPE_F32 = 1
    TI_ARGUMENT_TYPE_NDARRAY = 2
    TI_ARGUMENT_TYPE_TEXTURE = 3
    TI_ARGUMENT_TYPE_SCALAR = 4
    TI_ARGUMENT_TYPE_TENSOR = 5


class TiMemoryUsageFlags(IntEnum):
    """Usages of a memory allocation.

    Taichi requires kernel argument memories to be allocated with TI_MEMORY_USAGE_STORAGE_BIT.

    - **TI_MEMORY_USAGE_STORAGE_BIT**: The memory can be read/write accessed by any kernel.
    - **TI_MEMORY_USAGE_UNIFORM_BIT**: The memory can be used as a uniform buffer in graphics pipelines.
    - **TI_MEMORY_USAGE_VERTEX_BIT**: The memory can be used as a vertex buffer in graphics pipelines.
    - **TI_MEMORY_USAGE_INDEX_BIT**: The memory can be used as an index buffer in graphics pipelines.
    """

    TI_MEMORY_USAGE_STORAGE_BIT = _TiMemoryUsageFlagBits.TI_MEMORY_USAGE_STORAGE_BIT
    TI_MEMORY_USAGE_UNIFORM_BIT = _TiMemoryUsageFlagBits.TI_MEMORY_USAGE_UNIFORM_BIT
    TI_MEMORY_USAGE_VERTEX_BIT = _TiMemoryUsageFlagBits.TI_MEMORY_USAGE_VERTEX_BIT
    TI_MEMORY_USAGE_INDEX_BIT = _TiMemoryUsageFlagBits.TI_MEMORY_USAGE_INDEX_BIT


class TiImageUsageFlags(IntEnum):
    """Usages of an image allocation.

    - **TI_IMAGE_USAGE_STORAGE_BIT**: The image can be read/write accessed by any kernel.
    - **TI_IMAGE_USAGE_SAMPLED_BIT**: The image can be read-only accessed by any kernel.
    - **TI_IMAGE_USAGE_ATTACHMENT_BIT**: The image can be used as a color or depth-stencil attachment depending on its format.
    """

    TI_IMAGE_USAGE_STORAGE_BIT = _TiImageUsageFlagBits.TI_IMAGE_USAGE_STORAGE_BIT
    TI_IMAGE_USAGE_SAMPLED_BIT = _TiImageUsageFlagBits.TI_IMAGE_USAGE_SAMPLED_BIT
    TI_IMAGE_USAGE_ATTACHMENT_BIT = _TiImageUsageFlagBits.TI_IMAGE_USAGE_ATTACHMENT_BIT


class TiImageDimension(IntEnum):
    """Dimensions of an image allocation.

    - **TI_IMAGE_DIMENSION_1D**: 1-dimensional image.
    - **TI_IMAGE_DIMENSION_2D**: 2-dimensional image.
    - **TI_IMAGE_DIMENSION_3D**: 3-dimensional image.
    - **TI_IMAGE_DIMENSION_1D_ARRAY**: 1-dimensional image with one or more layers.
    - **TI_IMAGE_DIMENSION_2D_ARRAY**: 2-dimensional image with one or more layers.
    - **TI_IMAGE_DIMENSION_CUBE**: 2-dimensional image with 6 layers for faces towards +X, -X, +Y, -Y, +Z, -Z.
    """

    TI_IMAGE_DIMENSION_1D = 0
    TI_IMAGE_DIMENSION_2D = 1
    TI_IMAGE_DIMENSION_3D = 2
    TI_IMAGE_DIMENSION_1D_ARRAY = 3
    TI_IMAGE_DIMENSION_2D_ARRAY = 4
    TI_IMAGE_DIMENSION_CUBE = 5


class TiImageLayout(IntEnum):
    """Image layouts.

    - **TI_IMAGE_LAYOUT_UNDEFINED**: Undefined layout. An image in this layout does not contain any semantical information.
    - **TI_IMAGE_LAYOUT_SHADER_READ**: Optimal layout for read-only access, including sampling.
    - **TI_IMAGE_LAYOUT_SHADER_WRITE**: Optimal layout for write-only access.
    - **TI_IMAGE_LAYOUT_SHADER_READ_WRITE**: Optimal layout for read/write access.
    - **TI_IMAGE_LAYOUT_COLOR_ATTACHMENT**: Optimal layout as a color attachment.
    - **TI_IMAGE_LAYOUT_COLOR_ATTACHMENT_READ**: Optimal layout as an input color attachment.
    - **TI_IMAGE_LAYOUT_DEPTH_ATTACHMENT**: Optimal layout as a depth attachment.
    - **TI_IMAGE_LAYOUT_DEPTH_ATTACHMENT_READ**: Optimal layout as an input depth attachment.
    - **TI_IMAGE_LAYOUT_TRANSFER_DST**: Optimal layout as a data copy destination.
    - **TI_IMAGE_LAYOUT_TRANSFER_SRC**: Optimal layout as a data copy source.
    - **TI_IMAGE_LAYOUT_PRESENT_SRC**: Optimal layout as a presentation source.
    """

    TI_IMAGE_LAYOUT_UNDEFINED = 0
    TI_IMAGE_LAYOUT_SHADER_READ = 1
    TI_IMAGE_LAYOUT_SHADER_WRITE = 2
    TI_IMAGE_LAYOUT_SHADER_READ_WRITE = 3
    TI_IMAGE_LAYOUT_COLOR_ATTACHMENT = 4
    TI_IMAGE_LAYOUT_COLOR_ATTACHMENT_READ = 5
    TI_IMAGE_LAYOUT_DEPTH_ATTACHMENT = 6
    TI_IMAGE_LAYOUT_DEPTH_ATTACHMENT_READ = 7
    TI_IMAGE_LAYOUT_TRANSFER_DST = 8
    TI_IMAGE_LAYOUT_TRANSFER_SRC = 9
    TI_IMAGE_LAYOUT_PRESENT_SRC = 10


class TiFormat(IntEnum):
    """Texture formats.

    - **TI_FORMAT_UNKNOWN**: Unknown texture format.
    - **TI_FORMAT_R8**: 8-bit single-channel texture format.
    - **TI_FORMAT_RG8**: 8-bit two-channel texture format.
    - **TI_FORMAT_RGBA8**: 8-bit four-channel texture format.
    - **TI_FORMAT_RGBA8SRGB**: 8-bit four-channel SRGB texture format.
    - **TI_FORMAT_BGRA8**: 8-bit four-channel BGRA texture format.
    - **TI_FORMAT_BGRA8SRGB**: 8-bit four-channel BGRA SRGB texture format.
    - **TI_FORMAT_R8U**: Unsigned 8-bit single-channel texture format.
    - **TI_FORMAT_RG8U**: Unsigned 8-bit two-channel texture format.
    - **TI_FORMAT_RGBA8U**: Unsigned 8-bit four-channel texture format.
    - **TI_FORMAT_R8I**: Signed 8-bit single-channel texture format.
    - **TI_FORMAT_RG8I**: Signed 8-bit two-channel texture format.
    - **TI_FORMAT_RGBA8I**: Signed 8-bit four-channel texture format.
    - **TI_FORMAT_R16**: 16-bit single-channel texture format.
    - **TI_FORMAT_RG16**: 16-bit two-channel texture format.
    - **TI_FORMAT_RGB16**: 16-bit three-channel texture format.
    - **TI_FORMAT_RGBA16**: 16-bit four-channel texture format.
    - **TI_FORMAT_R16U**: Unsigned 16-bit single-channel texture format.
    - **TI_FORMAT_RG16U**: Unsigned 16-bit two-channel texture format.
    - **TI_FORMAT_RGB16U**: Unsigned 16-bit three-channel texture format.
    - **TI_FORMAT_RGBA16U**: Unsigned 16-bit four-channel texture format.
    - **TI_FORMAT_R16I**: Signed 16-bit single-channel texture format.
    - **TI_FORMAT_RG16I**: Signed 16-bit two-channel texture format.
    - **TI_FORMAT_RGB16I**: Signed 16-bit three-channel texture format.
    - **TI_FORMAT_RGBA16I**: Signed 16-bit four-channel texture format.
    - **TI_FORMAT_R16F**: 16-bit single-channel floating-point texture format.
    - **TI_FORMAT_RG16F**: 16-bit two-channel floating-point texture format.
    - **TI_FORMAT_RGB16F**: 16-bit three-channel floating-point texture format.
    - **TI_FORMAT_RGBA16F**: 16-bit four-channel floating-point texture format.
    - **TI_FORMAT_R32U**: Unsigned 32-bit single-channel texture format.
    - **TI_FORMAT_RG32U**: Unsigned 32-bit two-channel texture format.
    - **TI_FORMAT_RGB32U**: Unsigned 32-bit three-channel texture format.
    - **TI_FORMAT_RGBA32U**: Unsigned 32-bit four-channel texture format.
    - **TI_FORMAT_R32I**: Signed 32-bit single-channel texture format.
    - **TI_FORMAT_RG32I**: Signed 32-bit two-channel texture format.
    - **TI_FORMAT_RGB32I**: Signed 32-bit three-channel texture format.
    - **TI_FORMAT_RGBA32I**: Signed 32-bit four-channel texture format.
    - **TI_FORMAT_R32F**: 32-bit single-channel floating-point texture format.
    - **TI_FORMAT_RG32F**: 32-bit two-channel floating-point texture format.
    - **TI_FORMAT_RGB32F**: 32-bit three-channel floating-point texture format.
    - **TI_FORMAT_RGBA32F**: 32-bit four-channel floating-point texture format.
    - **TI_FORMAT_DEPTH16**: 16-bit depth texture format.
    - **TI_FORMAT_DEPTH24STENCIL8**: 24-bit depth, 8-bit stencil texture format.
    - **TI_FORMAT_DEPTH32F**: 32-bit floating-point depth texture format.
    """

    TI_FORMAT_UNKNOWN = 0
    TI_FORMAT_R8 = 1
    TI_FORMAT_RG8 = 2
    TI_FORMAT_RGBA8 = 3
    TI_FORMAT_RGBA8SRGB = 4
    TI_FORMAT_BGRA8 = 5
    TI_FORMAT_BGRA8SRGB = 6
    TI_FORMAT_R8U = 7
    TI_FORMAT_RG8U = 8
    TI_FORMAT_RGBA8U = 9
    TI_FORMAT_R8I = 10
    TI_FORMAT_RG8I = 11
    TI_FORMAT_RGBA8I = 12
    TI_FORMAT_R16 = 13
    TI_FORMAT_RG16 = 14
    TI_FORMAT_RGB16 = 15
    TI_FORMAT_RGBA16 = 16
    TI_FORMAT_R16U = 17
    TI_FORMAT_RG16U = 18
    TI_FORMAT_RGB16U = 19
    TI_FORMAT_RGBA16U = 20
    TI_FORMAT_R16I = 21
    TI_FORMAT_RG16I = 22
    TI_FORMAT_RGB16I = 23
    TI_FORMAT_RGBA16I = 24
    TI_FORMAT_R16F = 25
    TI_FORMAT_RG16F = 26
    TI_FORMAT_RGB16F = 27
    TI_FORMAT_RGBA16F = 28
    TI_FORMAT_R32U = 29
    TI_FORMAT_RG32U = 30
    TI_FORMAT_RGB32U = 31
    TI_FORMAT_RGBA32U = 32
    TI_FORMAT_R32I = 33
    TI_FORMAT_RG32I = 34
    TI_FORMAT_RGB32I = 35
    TI_FORMAT_RGBA32I = 36
    TI_FORMAT_R32F = 37
    TI_FORMAT_RG32F = 38
    TI_FORMAT_RGB32F = 39
    TI_FORMAT_RGBA32F = 40
    TI_FORMAT_DEPTH16 = 41
    TI_FORMAT_DEPTH24STENCIL8 = 42
    TI_FORMAT_DEPTH32F = 43


class TiFilter(IntEnum):
    """Texture filtering modes.

    - **TI_FILTER_NEAREST**: Nearest-neighbor filtering.
    - **TI_FILTER_LINEAR**: Linear filtering.
    """

    TI_FILTER_NEAREST = 0
    TI_FILTER_LINEAR = 1


class TiAddressMode(IntEnum):
    """Texture addressing modes.

    - **TI_ADDRESS_MODE_REPEAT**: Repeat addressing mode.
    - **TI_ADDRESS_MODE_MIRRORED_REPEAT**: Mirrored repeat addressing mode.
    - **TI_ADDRESS_MODE_CLAMP_TO_EDGE**: Clamp to edge addressing mode.
    """

    TI_ADDRESS_MODE_REPEAT = 0
    TI_ADDRESS_MODE_MIRRORED_REPEAT = 1
    TI_ADDRESS_MODE_CLAMP_TO_EDGE = 2
