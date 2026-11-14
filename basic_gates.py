def NOT(a):
    return (~a) & 1

def AND(a,b):
    return a & b 

def OR(a,b):
    return a | b

def XOR(a,b):
    return a ^ b

def NAND(a,b):
    return NOT(AND(a,b))

def NOR(a,b):
    return NOT(OR(a,b))