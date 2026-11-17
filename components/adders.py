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

        
