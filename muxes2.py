def mux2x1(a,b,sel):
    return OR(
        AND(a, NOT(sel)), 
        AND(b, sel))

def mux5x1(a,b,c,d,e,sel):
    return -1