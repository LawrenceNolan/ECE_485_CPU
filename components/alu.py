# here you go ricky, make a 1-bit ALU and then make it 32-bit

from components.gates import *
from components.adders import full_adder
from components.muxes import mux2, mux3

def alu_1bit(a: int, b: int, binvert: int, cin: int, op: int) -> tuple[int, int]:
    b_in = mux2(b, NOT(b), binvert)

    anding = AND(a, b_in)
    oring = OR(a, b_in)
    adding, cout = full_adder(a, b_in, cin)

    result = mux3(anding, oring, adding, op)
    return result, cout

def alu_32bit(a32: int, b32: int, binvert: int, op: int) -> tuple[int, int]:
    # 1. Initial carry-in
    cin = binvert
    result = 0

    # 2. Sequential 32 1-bit ALUs
    for i in range(32):
        a = (a32 >> i) & 1
        b = (b32 >> i) & 1

        bit_res, cin = alu_1bit(a, b, binvert, cin, op)
        result |= (bit_res << i)

    # 3. 32-input NOR gate - Zero flag
    or_all_bits = 0
    for i in range(32):
        bit = (result >> i) & 1
        or_all_bits = OR(or_all_bits, bit)
    zero = NOT(or_all_bits)

    return result, zero

#   notes:
#    Control Signals:
#      - ADD / LW / SW / PC+4 : binvert=0, op=2
#      - SUB / SUBI / BNE     : binvert=1, op=2
#      - ORI                  : binvert=0, op=1
#      - AND                  : binvert=0, op=0     