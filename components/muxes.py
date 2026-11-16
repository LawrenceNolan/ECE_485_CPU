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