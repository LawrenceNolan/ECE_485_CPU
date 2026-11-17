from components.gates import *
from components.muxes import *

def sign_extend(imm16: int) -> int:
    """
    Sign-extends a 16-bit immediate to a 32-bit integer bus.
    Replicates bit 15 (sign bit) across bits 16..31.
    Used by: lw, sw, bne offset, subi
    """
    sign_bit = (imm16 >> 15) & 1
    result = imm16 & 0xFFFF

    for i in range(16, 32):
        result |= (sign_bit << i)

    return result


def zero_extend(imm16: int) -> int:
    """
    Zero-extends a 16-bit immediate to a 32-bit integer bus.
    Pads bits 16..31 with 0s.
    Used by: ori
    """
    return imm16 & 0xFFFF


def extend_mux(imm16: int, ext_op: int) -> int:
    """
    Combined Immediate Extension Unit for ID-9 ISA:
      - ext_op = 0 : zero_extend (used for ori)
      - ext_op = 1 : sign_extend (used for lw, sw, bne, subi)
    """
    z_ext = zero_extend(imm16)
    s_ext = sign_extend(imm16)
    return mux2_32(z_ext, s_ext, ext_op)


def shift_left_2(bus32: int) -> int:
    """
    Shifts a 32-bit bus left by 2 bits (multiplies by 4)
    """
    return (bus32 << 2) & 0xFFFFFFFF