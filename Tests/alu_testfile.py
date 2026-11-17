import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))


# Start of testbench
from components.alu import *




def alu_tb():
    print("Running ALU Testbench...\n")


    # 1-Bit ALU signature: (a, b, cin, op)
    # Control encoding: binvert = (op >> 2) & 1, opm = (op >> 1) & 1
    # - OR  (op=0): binvert=0, opm=0 -> OR(a, b)
    # - ADD (op=2): binvert=0, opm=1 -> ADD(a, b, cin)
    # - SUB (op=6): binvert=1, opm=1 -> SUB(a, NOT(b), cin)


    # OR operation (op=0)
    assert alu_1bit(0, 0, 0, 0) == (0, 0), "alu_1bit OR(0, 0) failed"
    assert alu_1bit(0, 1, 0, 0) == (1, 0), "alu_1bit OR(0, 1) failed"
    assert alu_1bit(1, 0, 0, 0) == (1, 0), "alu_1bit OR(1, 0) failed"
    assert alu_1bit(1, 1, 0, 0) == (1, 1), "alu_1bit OR(1, 1) failed"


    # ADD operation (op=2)
    assert alu_1bit(0, 0, 0, 2) == (0, 0), "alu_1bit ADD(0, 0, cin=0) failed"
    assert alu_1bit(0, 1, 0, 2) == (1, 0), "alu_1bit ADD(0, 1, cin=0) failed"
    assert alu_1bit(1, 1, 0, 2) == (0, 1), "alu_1bit ADD(1, 1, cin=0) failed"
    assert alu_1bit(1, 1, 1, 2) == (1, 1), "alu_1bit ADD(1, 1, cin=1) failed"


    # SUB operation (op=6 -> binvert=1, opm=1)
    assert alu_1bit(1, 1, 1, 6) == (0, 1), "alu_1bit SUB(1, 1, cin=1) failed"
    assert alu_1bit(1, 0, 1, 6) == (1, 1), "alu_1bit SUB(1, 0, cin=1) failed"
    assert alu_1bit(0, 1, 1, 6) == (1, 0), "alu_1bit SUB(0, 1, cin=1) failed"
    print("alu_1bit passed")


    # 32-Bit ALU signature: (a32, b32, op)
    # ADD (op=2)
    assert alu_32bit(0, 0, 2) == (0, 1), "alu_32bit ADD(0, 0) failed"
    assert alu_32bit(100, 300, 2) == (400, 0), "alu_32bit ADD(100, 300) failed"
    assert alu_32bit(0x7FFFFFFF, 1, 2) == (0x80000000, 0), "alu_32bit MSB carry failed"
    assert alu_32bit(0xFFFFFFFF, 1, 2) == (0, 1), "alu_32bit ripple wrap zero flag failed"


    # SUB / SUBI / BNE (op=6)
    assert alu_32bit(125, 25, 6) == (100, 0), "alu_32bit SUBI(125, 25) failed"
    assert alu_32bit(75, 75, 6) == (0, 1), "alu_32bit BNE equal zero flag failed"
    assert alu_32bit(10, 125, 6) == (0xFFFFFF8D, 0), "alu_32bit BNE unequal negative result failed"


    # OR / ORI (op=0)
    assert alu_32bit(0, 0, 0) == (0, 1), "alu_32bit ORI(0, 0) failed"
    assert alu_32bit(0x00F0, 0x000F, 0) == (0x00FF, 0), "alu_32bit ORI(0x00F0, 0x000F) failed"
    print("alu_32bit passed")


    print("\nAll Tests Passed")




try:
    alu_tb()


except Exception as error:
    print(error)


finally:
    print("Simulation Complete")