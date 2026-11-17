from components.gates import *

def mux2(i0,i1,sel):

    d0 = AND(i0,NOT(sel))
    d1 = AND(i1, sel)

    return OR(d0,d1)


def mux3(i0,i1,i2,sel):
    
    # Extracting each bit
    s0 = sel & 1 
    s1 = (sel >> 1) & 1

    # Invertered sel bits
    not_s0 = NOT(s0)
    not_s1 = NOT(s1)

    # 00-10 -> i0-i2
    d0 = AND3(i0, not_s1, not_s0)
    d1 = AND3(i1, not_s1, s0)
    d2 = AND3(i2, s1, not_s0)

    return OR3(d0,d1,d2)


def mux4(i0,i1,i2,i3,sel):
    
    # Extracting each bit
    s0 = sel & 1 
    s1 = (sel >> 1) & 1

    # Invertered sel bits
    not_s0 = NOT(s0)
    not_s1 = NOT(s1)

    # 00-11 -> i0-i3
    d0 = AND3(i0, not_s1, not_s0)
    d1 = AND3(i1, not_s1, s0)
    d2 = AND3(i2, s1, not_s0)
    d3 = AND3(i3, s1, s0)

    return OR4(d0,d1,d2,d3)
    

def mux5(i0,i1,i2,i3,i4,sel):

    # Extracting each bit
    s0 = sel & 1
    s1 = (sel >> 1) & 1
    s2 = (sel >> 2) & 1

    # Inverted sel bits
    not_s0 = NOT(s0)
    not_s1 = NOT(s1)
    not_s2 = NOT(s2)

    # 000-100 -> i0-i4
    d0 = AND4(i0, not_s2, not_s1, not_s0)
    d1 = AND4(i1, not_s2, not_s1, s0)
    d2 = AND4(i2, not_s2, s1, not_s0)
    d3 = AND4(i3, not_s2, s1, s0)
    d4 = AND4(i4, s2, not_s1, not_s0)

    return OR5(d0,d1,d2,d3,d4)

def mux2_32(a32: int, b32: int, sel: int) -> int:
    result = 0
    for i in range(32):
        a = (a32 >> i) & 1
        b = (b32 >> i) & 1
        bit = mux2(a, b, sel)
        result |= (bit << i)
    return result

def mux3_32(a32: int, b32: int, c32: int, sel: int) -> int:
    result = 0
    for i in range(32):
        a = (a32 >> i) & 1
        b = (b32 >> i) & 1
        c = (c32 >> i) & 1
        bit = mux3(a, b, c, sel)
        result |= (bit << i)
    return result

def mux4_32(a32: int, b32: int, c32: int, d32: int, sel: int) -> int:
    result = 0
    for i in range(32):
        a = (a32 >> i) & 1
        b = (b32 >> i) & 1
        c = (c32 >> i) & 1
        d = (d32 >> i) & 1
        bit = mux4(a, b, c, d, sel)
        result |= (bit << i)
    return result