from ctypes import c_int


class TiBool(c_int):
    """A boolean value. Can be either TI_TRUE or TI_FALSE.
     Assignment with other values could lead to undefined behavior."""
    pass


class TiFlags(c_int):
    """A bit field that can be used to represent 32 orthogonal flags.
     Bits unspecified in the corresponding flag enum are ignored."""
    pass