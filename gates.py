# basic gates

def NOT(a):
    return (~a) & 1

def AND(a,b):
    return (a & b) & 1

def OR(a,b):
    return a | b

def XOR(a,b):
    return a ^ b

def NAND(a,b):
    return NOT(AND(a,b))

def NOR(a,b):
    return NOT(OR(a,b))


# helper gates

def AND3(a,b,c):
    return AND(AND(a,b), c)

def AND4(a,b,c,d):
    return AND(AND(a,b), AND(c,d))

def OR5(a,b,c,d,e):
    return OR(OR(OR(a,b), OR(c,d)), e)