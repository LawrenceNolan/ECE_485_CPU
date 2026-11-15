from gates import *


#tests
def gates_tb():
    print("Gate Testbench\n")

    print("NOT gate:")
    print(NOT(0))
    print(NOT(1))

    print("\nAND gate:")
    print(AND(0,0))
    print(AND(0,1))
    print(AND(1,0))
    print(AND(1,1))

    print("\nOR gate:")
    print(OR(0,0))
    print(OR(0,1))
    print(OR(1,0))
    print(OR(1,1))

    print("\nXOR gate:")
    print(XOR(0,0))
    print(XOR(0,1))
    print(XOR(1,0))
    print(XOR(1,1))

    print("\nNAND gate:")
    print(NAND(0,0))
    print(NAND(0,1))
    print(NAND(1,0))
    print(NAND(1,1))

    print("\nNOR gate:")
    print(NOR(0,0))
    print(NOR(0,1))
    print(NOR(1,0))
    print(NOR(1,1))

    print("SIMULATION COMPLETE")


#run
gates_tb()