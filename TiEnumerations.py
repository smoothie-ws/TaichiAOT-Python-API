from ctypes import c_int


class TiError(c_int):
    """Errors reported by the Taichi C-API."""

    TI_ERROR_SUCCESS = 0  # Successful Taichi C-API invocation.
    TI_ERROR_NOT_SUPPORTED = -1  # API or parameter combination not supported.
    TI_ERROR_CORRUPTED_DATA = -2  # Provided data is corrupted.
    TI_ERROR_NAME_NOT_FOUND = -3  # Provided name does not exist.
    TI_ERROR_INVALID_ARGUMENT = -4  # Function argument constraint violation or AOT module kernel argument mismatch.
    TI_ERROR_ARGUMENT_NULL = -5  # One or more by-reference (pointer) function arguments point to null.
    TI_ERROR_ARGUMENT_OUT_OF_RANGE = -6  # One or more function arguments are out of its acceptable range.
    TI_ERROR_ARGUMENT_NOT_FOUND = -7  # One or more kernel arguments are missing.
    TI_ERROR_INVALID_INTEROP = -8  # The intended interoperation is not possible on the current arch.
    TI_ERROR_INVALID_STATE = -9  # The Taichi C-API enters an unrecoverable invalid state.
    TI_ERROR_INCOMPATIBLE_MODULE = -10  # The AOT module is not compatible with the current runtime.
    TI_ERROR_OUT_OF_MEMORY = -11  # Out of memory.
    TI_ERROR_MAX_ENUM = 0xffffffff  # Maximum value of the enumeration.


class TiArch(c_int):
    """Types of backend archs."""

    TI_ARCH_RESERVED = 0  # Reserved backend architecture.
    TI_ARCH_VULKAN = 1  # Vulkan backend architecture.
    TI_ARCH_METAL = 2  # Metal backend architecture.
    TI_ARCH_CUDA = 3  # CUDA backend architecture.
    TI_ARCH_X64 = 4  # x86-64 backend architecture.
    TI_ARCH_ARM64 = 5  # ARM64 backend architecture.
    TI_ARCH_OPENGL = 6  # OpenGL backend architecture.
    TI_ARCH_GLES = 7  # OpenGL ES backend architecture.
    TI_ARCH_MAX_ENUM = 0xffffffff  # Maximum value of the enumeration.


class TiCapability(c_int):
    """Device capabilities."""

    TI_CAPABILITY_RESERVED = 0  # Reserved device capability.
    TI_CAPABILITY_SPIRV_VERSION = 1  # SPIR-V version capability.
    TI_CAPABILITY_SPIRV_HAS_INT8 = 2  # SPIR-V capability: supports int8.
    TI_CAPABILITY_SPIRV_HAS_INT16 = 3  # SPIR-V capability: supports int16.
    TI_CAPABILITY_SPIRV_HAS_INT64 = 4  # SPIR-V capability: supports int64.
    TI_CAPABILITY_SPIRV_HAS_FLOAT16 = 5  # SPIR-V capability: supports float16.
    TI_CAPABILITY_SPIRV_HAS_FLOAT64 = 6  # SPIR-V capability: supports float64.
    TI_CAPABILITY_SPIRV_HAS_ATOMIC_INT64 = 7  # SPIR-V capability: supports atomic operations on int64.
    TI_CAPABILITY_SPIRV_HAS_ATOMIC_FLOAT16 = 8  # SPIR-V capability: supports atomic operations on float16.
    TI_CAPABILITY_SPIRV_HAS_ATOMIC_FLOAT16_ADD = 9  # SPIR-V capability: supports atomic add on float16.
    TI_CAPABILITY_SPIRV_HAS_ATOMIC_FLOAT16_MINMAX = 10  # SPIR-V capability: supports atomic min/max on float16.
    TI_CAPABILITY_SPIRV_HAS_ATOMIC_FLOAT = 11  # SPIR-V capability: supports atomic operations on float.
    TI_CAPABILITY_SPIRV_HAS_ATOMIC_FLOAT_ADD = 12  # SPIR-V capability: supports atomic add on float.
    TI_CAPABILITY_SPIRV_HAS_ATOMIC_FLOAT_MINMAX = 13  # SPIR-V capability: supports atomic min/max on float.
    TI_CAPABILITY_SPIRV_HAS_ATOMIC_FLOAT64 = 14  # SPIR-V capability: supports atomic operations on float64.
    TI_CAPABILITY_SPIRV_HAS_ATOMIC_FLOAT64_ADD = 15  # SPIR-V capability: supports atomic add on float64.
    TI_CAPABILITY_SPIRV_HAS_ATOMIC_FLOAT64_MINMAX = 16  # SPIR-V capability: supports atomic min/max on float64.
    TI_CAPABILITY_SPIRV_HAS_VARIABLE_PTR = 17  # SPIR-V capability: supports variable pointer.
    TI_CAPABILITY_SPIRV_HAS_PHYSICAL_STORAGE_BUFFER = 18  # SPIR-V capability: supports physical storage buffer.
    TI_CAPABILITY_SPIRV_HAS_SUBGROUP_BASIC = 19  # SPIR-V capability: supports basic subgroup operations.
    TI_CAPABILITY_SPIRV_HAS_SUBGROUP_VOTE = 20  # SPIR-V capability: supports subgroup vote operations.
    TI_CAPABILITY_SPIRV_HAS_SUBGROUP_ARITHMETIC = 21  # SPIR-V capability: supports subgroup arithmetic operations.
    TI_CAPABILITY_SPIRV_HAS_SUBGROUP_BALLOT = 22  # SPIR-V capability: supports subgroup ballot operations.
    TI_CAPABILITY_SPIRV_HAS_NON_SEMANTIC_INFO = 23  # SPIR-V capability: supports non-semantic information.
    TI_CAPABILITY_SPIRV_HAS_NO_INTEGER_WRAP_DECORATION = 24  # SPIR-V capability: does not have integer wrap decoration.
    TI_CAPABILITY_MAX_ENUM = 0xffffffff  # Maximum value of the enumeration.


class TiDataType(c_int):
    """Elementary (primitive) data types in the Taichi C-API.

    There might be vendor-specific constraints on the available data types,
    so it's recommended to use 32-bit data types if multi-platform distribution is desired.
    """

    TI_DATA_TYPE_F16 = 0  # 16-bit IEEE 754 half-precision floating-point number.
    TI_DATA_TYPE_F32 = 1  # 32-bit IEEE 754 single-precision floating-point number.
    TI_DATA_TYPE_F64 = 2  # 64-bit IEEE 754 double-precision floating-point number.
    TI_DATA_TYPE_I8 = 3  # 8-bit one's complement signed integer.
    TI_DATA_TYPE_I16 = 4  # 16-bit one's complement signed integer.
    TI_DATA_TYPE_I32 = 5  # 32-bit one's complement signed integer.
    TI_DATA_TYPE_I64 = 6  # 64-bit one's complement signed integer.
    TI_DATA_TYPE_U1 = 7  # 1-bit unsigned integer.
    TI_DATA_TYPE_U8 = 8  # 8-bit unsigned integer.
    TI_DATA_TYPE_U16 = 9  # 16-bit unsigned integer.
    TI_DATA_TYPE_U32 = 10  # 32-bit unsigned integer.
    TI_DATA_TYPE_U64 = 11  # 64-bit unsigned integer.
    TI_DATA_TYPE_GEN = 12  # Generic data type.
    TI_DATA_TYPE_UNKNOWN = 13  # Unknown data type.
    TI_DATA_TYPE_MAX_ENUM = 0xffffffff  # Maximum value of the enumeration.


class TiArgumentType(c_int):
    """Types of kernel and compute graph arguments in the Taichi C-API."""

    TI_ARGUMENT_TYPE_I32 = 0  # 32-bit one's complement signed integer.
    TI_ARGUMENT_TYPE_F32 = 1  # 32-bit IEEE 754 single-precision floating-point number.
    TI_ARGUMENT_TYPE_NDARRAY = 2  # ND-array wrapped around a `handle.memory`.
    TI_ARGUMENT_TYPE_TEXTURE = 3  # Texture wrapped around a `handle.image`.
    TI_ARGUMENT_TYPE_SCALAR = 4  # Typed scalar.
    TI_ARGUMENT_TYPE_TENSOR = 5  # Typed tensor.
    TI_ARGUMENT_TYPE_MAX_ENUM = 0xffffffff  # Maximum value of the enumeration.


class TiMemoryUsageFlagBits(c_int):
    """Usages of a memory allocation.
    Taichi requires kernel argument memories to be allocated with TI_MEMORY_USAGE_STORAGE_BIT."""

    TI_MEMORY_USAGE_STORAGE_BIT = 1 << 0  # The memory can be read/write accessed by any kernel.
    TI_MEMORY_USAGE_UNIFORM_BIT = 1 << 1  # The memory can be used as a uniform buffer in graphics pipelines.
    TI_MEMORY_USAGE_VERTEX_BIT = 1 << 2  # The memory can be used as a vertex buffer in graphics pipelines.
    TI_MEMORY_USAGE_INDEX_BIT = 1 << 3  # The memory can be used as an index buffer in graphics pipelines.


class TiMemoryUsageFlags(c_int):
    TI_MEMORY_USAGE_STORAGE_BIT = TiMemoryUsageFlagBits.TI_MEMORY_USAGE_STORAGE_BIT
    TI_MEMORY_USAGE_UNIFORM_BIT = TiMemoryUsageFlagBits.TI_MEMORY_USAGE_UNIFORM_BIT
    TI_MEMORY_USAGE_VERTEX_BIT = TiMemoryUsageFlagBits.TI_MEMORY_USAGE_VERTEX_BIT
    TI_MEMORY_USAGE_INDEX_BIT = TiMemoryUsageFlagBits.TI_MEMORY_USAGE_INDEX_BIT


class TiImageUsageFlagBits(c_int):
    """Usages of an image allocation in the Taichi C-API."""

    TI_IMAGE_USAGE_STORAGE_BIT = 1 << 0  # The image can be read/write accessed by any kernel.
    TI_IMAGE_USAGE_SAMPLED_BIT = 1 << 1  # The image can be read-only accessed by any kernel.
    TI_IMAGE_USAGE_ATTACHMENT_BIT = 1 << 2  # The image can be used as a color or depth-stencil attachment depending on its format.


class TiImageUsageFlags(c_int):
    TI_IMAGE_USAGE_STORAGE_BIT = TiImageUsageFlagBits.TI_IMAGE_USAGE_STORAGE_BIT
    TI_IMAGE_USAGE_SAMPLED_BIT = TiImageUsageFlagBits.TI_IMAGE_USAGE_SAMPLED_BIT
    TI_IMAGE_USAGE_ATTACHMENT_BIT = TiImageUsageFlagBits.TI_IMAGE_USAGE_ATTACHMENT_BIT


class TiImageDimension(c_int):
    """Dimensions of an image allocation in the Taichi C-API."""

    TI_IMAGE_DIMENSION_1D = 0  # The image is 1-dimensional.
    TI_IMAGE_DIMENSION_2D = 1  # The image is 2-dimensional.
    TI_IMAGE_DIMENSION_3D = 2  # The image is 3-dimensional.
    TI_IMAGE_DIMENSION_1D_ARRAY = 3  # The image is 1-dimensional and has one or more layers.
    TI_IMAGE_DIMENSION_2D_ARRAY = 4  # The image is 2-dimensional and has one or more layers.
    TI_IMAGE_DIMENSION_CUBE = 5  # The image is 2-dimensional and has 6 layers for the faces towards +X, -X, +Y, -Y, +Z, -Z in sequence.
    TI_IMAGE_DIMENSION_MAX_ENUM = 0xffffffff  # Maximum value of the enumeration.


class TiImageLayout(c_int):
    """Image layouts in the Taichi C-API (1.4.0)."""

    TI_IMAGE_LAYOUT_UNDEFINED = 0  # Undefined layout. An image in this layout does not contain any semantical information.
    TI_IMAGE_LAYOUT_SHADER_READ = 1  # Optimal layout for read-only access, including sampling.
    TI_IMAGE_LAYOUT_SHADER_WRITE = 2  # Optimal layout for write-only access.
    TI_IMAGE_LAYOUT_SHADER_READ_WRITE = 3  # Optimal layout for read/write access.
    TI_IMAGE_LAYOUT_COLOR_ATTACHMENT = 4  # Optimal layout as a color attachment.
    TI_IMAGE_LAYOUT_COLOR_ATTACHMENT_READ = 5  # Optimal layout as an input color attachment.
    TI_IMAGE_LAYOUT_DEPTH_ATTACHMENT = 6  # Optimal layout as a depth attachment.
    TI_IMAGE_LAYOUT_DEPTH_ATTACHMENT_READ = 7  # Optimal layout as an input depth attachment.
    TI_IMAGE_LAYOUT_TRANSFER_DST = 8  # Optimal layout as a data copy destination.
    TI_IMAGE_LAYOUT_TRANSFER_SRC = 9  # Optimal layout as a data copy source.
    TI_IMAGE_LAYOUT_PRESENT_SRC = 10  # Optimal layout as a presentation source.
    TI_IMAGE_LAYOUT_MAX_ENUM = 0xffffffff  # Maximum value of the enumeration.


class TiFormat(c_int):
    """Texture formats in the Taichi C-API."""

    TI_FORMAT_UNKNOWN = 0  # Unknown texture format.
    TI_FORMAT_R8 = 1  # 8-bit single-channel texture format.
    TI_FORMAT_RG8 = 2  # 8-bit two-channel texture format.
    TI_FORMAT_RGBA8 = 3  # 8-bit four-channel texture format.
    TI_FORMAT_RGBA8SRGB = 4  # 8-bit four-channel SRGB texture format.
    TI_FORMAT_BGRA8 = 5  # 8-bit four-channel BGRA texture format.
    TI_FORMAT_BGRA8SRGB = 6  # 8-bit four-channel BGRA SRGB texture format.
    TI_FORMAT_R8U = 7  # Unsigned 8-bit single-channel texture format.
    TI_FORMAT_RG8U = 8  # Unsigned 8-bit two-channel texture format.
    TI_FORMAT_RGBA8U = 9  # Unsigned 8-bit four-channel texture format.
    TI_FORMAT_R8I = 10  # Signed 8-bit single-channel texture format.
    TI_FORMAT_RG8I = 11  # Signed 8-bit two-channel texture format.
    TI_FORMAT_RGBA8I = 12  # Signed 8-bit four-channel texture format.
    TI_FORMAT_R16 = 13  # 16-bit single-channel texture format.
    TI_FORMAT_RG16 = 14  # 16-bit two-channel texture format.
    TI_FORMAT_RGB16 = 15  # 16-bit three-channel texture format.
    TI_FORMAT_RGBA16 = 16  # 16-bit four-channel texture format.
    TI_FORMAT_R16U = 17  # Unsigned 16-bit single-channel texture format.
    TI_FORMAT_RG16U = 18  # Unsigned 16-bit two-channel texture format.
    TI_FORMAT_RGB16U = 19  # Unsigned 16-bit three-channel texture format.
    TI_FORMAT_RGBA16U = 20  # Unsigned 16-bit four-channel texture format.
    TI_FORMAT_R16I = 21  # Signed 16-bit single-channel texture format.
    TI_FORMAT_RG16I = 22  # Signed 16-bit two-channel texture format.
    TI_FORMAT_RGB16I = 23  # Signed 16-bit three-channel texture format.
    TI_FORMAT_RGBA16I = 24  # Signed 16-bit four-channel texture format.
    TI_FORMAT_R16F = 25  # 16-bit single-channel floating-point texture format.
    TI_FORMAT_RG16F = 26  # 16-bit two-channel floating-point texture format.
    TI_FORMAT_RGB16F = 27  # 16-bit three-channel floating-point texture format.
    TI_FORMAT_RGBA16F = 28  # 16-bit four-channel floating-point texture format.
    TI_FORMAT_R32U = 29  # Unsigned 32-bit single-channel texture format.
    TI_FORMAT_RG32U = 30  # Unsigned 32-bit two-channel texture format.
    TI_FORMAT_RGB32U = 31  # Unsigned 32-bit three-channel texture format.
    TI_FORMAT_RGBA32U = 32  # Unsigned 32-bit four-channel texture format.
    TI_FORMAT_R32I = 33  # Signed 32-bit single-channel texture format.
    TI_FORMAT_RG32I = 34  # Signed 32-bit two-channel texture format.
    TI_FORMAT_RGB32I = 35  # Signed 32-bit three-channel texture format.
    TI_FORMAT_RGBA32I = 36  # Signed 32-bit four-channel texture format.
    TI_FORMAT_R32F = 37  # 32-bit single-channel floating-point texture format.
    TI_FORMAT_RG32F = 38  # 32-bit two-channel floating-point texture format.
    TI_FORMAT_RGB32F = 39  # 32-bit three-channel floating-point texture format.
    TI_FORMAT_RGBA32F = 40  # 32-bit four-channel floating-point texture format.
    TI_FORMAT_DEPTH16 = 41  # 16-bit depth texture format.
    TI_FORMAT_DEPTH24STENCIL8 = 42  # 24-bit depth, 8-bit stencil texture format.
    TI_FORMAT_DEPTH32F = 43  # 32-bit floating-point depth texture format.
    TI_FORMAT_MAX_ENUM = 0xffffffff  # Maximum value of the enumeration.


class TiFilter(c_int):
    """Texture filtering modes."""

    TI_FILTER_NEAREST = 0  # Nearest-neighbor filtering.
    TI_FILTER_LINEAR = 1  # Linear filtering.
    TI_FILTER_MAX_ENUM = 0xffffffff  # Maximum value of the enumeration.


class TiAddressMode(c_int):
    """Texture addressing modes."""

    TI_ADDRESS_MODE_REPEAT = 0  # Repeat addressing mode.
    TI_ADDRESS_MODE_MIRRORED_REPEAT = 1  # Mirrored repeat addressing mode.
    TI_ADDRESS_MODE_CLAMP_TO_EDGE = 2  # Clamp to edge addressing mode.
    TI_ADDRESS_MODE_MAX_ENUM = 0xffffffff  # Maximum value of the enumeration.
