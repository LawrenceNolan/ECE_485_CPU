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


# helper gates (for the muxes)

def AND3(a,b,c):
    return AND(AND(a,b), c)

def AND4(a,b,c,d):
    return AND(AND(a,b), AND(c,d))

def OR3(a,b,c):
    return OR(OR(a,b), c)

def OR4(a,b,c,d):
    return OR(OR(a,b), OR(c,d))

def OR5(a,b,c,d,e):
    return OR(OR(OR(a,b), OR(c,d)), e)

# made for the zero flag for bne 
def NOR32(bus):

    result = 0
    for i in range(32):
        c1 = (bus >> i) & 1
        result = OR(result, c1)

    return NOT(result)

