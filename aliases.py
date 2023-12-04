from ctypes import c_uint32


class TiBool(c_uint32):
    """A boolean value. Can be either TI_TRUE or TI_FALSE.
     Assignment with other values could lead to undefined behavior."""
    pass


class TiFlags(c_uint32):
    """A bit field that can be used to represent 32 orthogonal flags.
     Bits unspecified in the corresponding flag enum are ignored."""
    pass