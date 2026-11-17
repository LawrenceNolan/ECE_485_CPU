# here you go ricky, make a 1-bit ALU and then make it 32-bit

from components.gates import *
from components.adders import full_adder
from components.muxes import mux2, mux3

def alu_1bit(a: int, b: int, cin: int, op: int) -> tuple[int, int]:
    opm = (op >> 1) & 1
    binvert = (op >> 2) & 1
    b_in = mux2(b, NOT(b), binvert)

    oring = OR(a, b_in)
    adding, cout = full_adder(a, b_in, cin)

    result = mux2(oring, adding, opm)
    return result, cout

def alu_32bit(a32: int, b32: int, op: int) -> tuple[int, int]:
    # 1. Initial carry-in
    cin = (op >> 2) & 1
    result = 0

    # 2. Sequential 32 1-bit ALUs
    for i in range(32):
        a = (a32 >> i) & 1
        b = (b32 >> i) & 1

        bit_res, cin = alu_1bit(a, b, cin, op)
        result |= (bit_res << i)

    # 3. 32-input NOR gate - Zero flag

    zero = NOR32(result)

    return result, zero

#   notes:
#    Control Signals:
#      - ADD / LW / SW / PC+4 / Branch Target   : binvert=0, op=1
#      - SUBI / BNE                             : binvert=1, op=1
#      - ORI                                    : binvert=0, op=0  
