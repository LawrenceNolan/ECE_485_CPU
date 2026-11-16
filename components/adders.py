from components.gates import *

def half_adder(a,b):
    S = XOR(a,b)
    Cout = AND(a,b)

    return S, Cout

def full_adder(a,b, Cin):
    sum1, c1 = half_adder(a,b)
    S, c2 = half_adder(sum1, Cin) 
    Cout = OR(c1,c2)

    return S, Cout

# This implementation uses a Ripple Carry Adder (RCA)
def adder_32(a32, b32, Cin=0):
    result = 0

    for i in range(32):
        a = (a32 >> i) & 1
        b = (b32 >> i) & 1

        S, Cin = full_adder(a,b, Cin)
        result |= (S << i)

    return result, Cin

        
