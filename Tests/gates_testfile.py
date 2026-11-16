# Looks one file higher so python can run these files
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

# Start of testbench
from components.gates import *


def gates_tb():
    print("Running Gate Testbench...\n")

    # NOT
    assert NOT(0) == 1, "NOT(0) failed"
    assert NOT(1) == 0, "NOT(1) failed"
    print("NOT gate passed")

    # AND
    assert AND(0, 0) == 0, "AND(0, 0) failed"
    assert AND(0, 1) == 0, "AND(0, 1) failed"
    assert AND(1, 0) == 0, "AND(1, 0) failed"
    assert AND(1, 1) == 1, "AND(1, 1) failed"
    print("AND gate passed")

    # OR
    assert OR(0, 0) == 0, "OR(0, 0) failed"
    assert OR(0, 1) == 1, "OR(0, 1) failed"
    assert OR(1, 0) == 1, "OR(1, 0) failed"
    assert OR(1, 1) == 1, "OR(1, 1) failed"
    print("OR gate passed")

    # XOR
    assert XOR(0, 0) == 0, "XOR(0, 0) failed"
    assert XOR(0, 1) == 1, "XOR(0, 1) failed"
    assert XOR(1, 0) == 1, "XOR(1, 0) failed"
    assert XOR(1, 1) == 0, "XOR(1, 1) failed"
    print("XOR gate passed")

    # NAND
    assert NAND(0, 0) == 1, "NAND(0, 0) failed"
    assert NAND(0, 1) == 1, "NAND(0, 1) failed"
    assert NAND(1, 0) == 1, "NAND(1, 0) failed"
    assert NAND(1, 1) == 0, "NAND(1, 1) failed"
    print("NAND gate passed")

    # NOR
    assert NOR(0, 0) == 1, "NOR(0, 0) failed"
    assert NOR(0, 1) == 0, "NOR(0, 1) failed"
    assert NOR(1, 0) == 0, "NOR(1, 0) failed"
    assert NOR(1, 1) == 0, "NOR(1, 1) failed"
    print("NOR gate passed")

    # Helper functions

    # AND3
    assert AND3(0, 0, 0) == 0, "AND3(0, 0, 0) failed"
    assert AND3(0, 0, 1) == 0, "AND3(0, 0, 1) failed"
    assert AND3(0, 1, 0) == 0, "AND3(0, 1, 0) failed"
    assert AND3(0, 1, 1) == 0, "AND3(0, 1, 1) failed"
    assert AND3(1, 0, 0) == 0, "AND3(1, 0, 0) failed"
    assert AND3(1, 0, 1) == 0, "AND3(1, 0, 1) failed"
    assert AND3(1, 1, 0) == 0, "AND3(1, 1, 0) failed"
    assert AND3(1, 1, 1) == 1, "AND3(1, 1, 1) failed"
    print("AND3 gate passed")

    # AND4
    assert AND4(0, 0, 0, 0) == 0, "AND4(0, 0, 0, 0) failed"
    assert AND4(0, 0, 0, 1) == 0, "AND4(0, 0, 0, 1) failed"
    assert AND4(0, 0, 1, 0) == 0, "AND4(0, 0, 1, 0) failed"
    assert AND4(0, 0, 1, 1) == 0, "AND4(0, 0, 1, 1) failed"
    assert AND4(0, 1, 0, 0) == 0, "AND4(0, 1, 0, 0) failed"
    assert AND4(0, 1, 0, 1) == 0, "AND4(0, 1, 0, 1) failed"
    assert AND4(0, 1, 1, 0) == 0, "AND4(0, 1, 1, 0) failed"
    assert AND4(0, 1, 1, 1) == 0, "AND4(0, 1, 1, 1) failed"
    assert AND4(1, 0, 0, 0) == 0, "AND4(1, 0, 0, 0) failed"
    assert AND4(1, 0, 0, 1) == 0, "AND4(1, 0, 0, 1) failed"
    assert AND4(1, 0, 1, 0) == 0, "AND4(1, 0, 1, 0) failed"
    assert AND4(1, 0, 1, 1) == 0, "AND4(1, 0, 1, 1) failed"
    assert AND4(1, 1, 0, 0) == 0, "AND4(1, 1, 0, 0) failed"
    assert AND4(1, 1, 0, 1) == 0, "AND4(1, 1, 0, 1) failed"
    assert AND4(1, 1, 1, 0) == 0, "AND4(1, 1, 1, 0) failed"
    assert AND4(1, 1, 1, 1) == 1, "AND4(1, 1, 1, 1) failed"
    print("AND4 gate passed")

    # OR3
    assert OR3(0, 0, 0) == 0, "OR3(0, 0, 0) failed"
    assert OR3(0, 0, 1) == 1, "OR3(0, 0, 1) failed"
    assert OR3(0, 1, 0) == 1, "OR3(0, 1, 0) failed"
    assert OR3(0, 1, 1) == 1, "OR3(0, 1, 1) failed"
    assert OR3(1, 0, 0) == 1, "OR3(1, 0, 0) failed"
    assert OR3(1, 0, 1) == 1, "OR3(1, 0, 1) failed"
    assert OR3(1, 1, 0) == 1, "OR3(1, 1, 0) failed"
    assert OR3(1, 1, 1) == 1, "OR3(1, 1, 1) failed"
    print("OR3 gate passed")

    # OR4
    assert OR4(0, 0, 0, 0) == 0, "OR4(0, 0, 0, 0) failed"
    assert OR4(0, 0, 0, 1) == 1, "OR4(0, 0, 0, 1) failed"
    assert OR4(0, 0, 1, 0) == 1, "OR4(0, 0, 1, 0) failed"
    assert OR4(0, 0, 1, 1) == 1, "OR4(0, 0, 1, 1) failed"
    assert OR4(0, 1, 0, 0) == 1, "OR4(0, 1, 0, 0) failed"
    assert OR4(0, 1, 0, 1) == 1, "OR4(0, 1, 0, 1) failed"
    assert OR4(0, 1, 1, 0) == 1, "OR4(0, 1, 1, 0) failed"
    assert OR4(0, 1, 1, 1) == 1, "OR4(0, 1, 1, 1) failed"
    assert OR4(1, 0, 0, 0) == 1, "OR4(1, 0, 0, 0) failed"
    assert OR4(1, 0, 0, 1) == 1, "OR4(1, 0, 0, 1) failed"
    assert OR4(1, 0, 1, 0) == 1, "OR4(1, 0, 1, 0) failed"
    assert OR4(1, 0, 1, 1) == 1, "OR4(1, 0, 1, 1) failed"
    assert OR4(1, 1, 0, 0) == 1, "OR4(1, 1, 0, 0) failed"
    assert OR4(1, 1, 0, 1) == 1, "OR4(1, 1, 0, 1) failed"
    assert OR4(1, 1, 1, 0) == 1, "OR4(1, 1, 1, 0) failed"
    assert OR4(1, 1, 1, 1) == 1, "OR4(1, 1, 1, 1) failed"
    print("OR4 gate passed")

    # OR5
    assert OR5(0, 0, 0, 0, 0) == 0, "OR5(0, 0, 0, 0, 0) failed"
    assert OR5(0, 0, 0, 0, 1) == 1, "OR5(0, 0, 0, 0, 1) failed"
    assert OR5(0, 0, 0, 1, 0) == 1, "OR5(0, 0, 0, 1, 0) failed"
    assert OR5(0, 0, 0, 1, 1) == 1, "OR5(0, 0, 0, 1, 1) failed"
    assert OR5(0, 0, 1, 0, 0) == 1, "OR5(0, 0, 1, 0, 0) failed"
    assert OR5(0, 0, 1, 0, 1) == 1, "OR5(0, 0, 1, 0, 1) failed"
    assert OR5(0, 0, 1, 1, 0) == 1, "OR5(0, 0, 1, 1, 0) failed"
    assert OR5(0, 0, 1, 1, 1) == 1, "OR5(0, 0, 1, 1, 1) failed"
    assert OR5(0, 1, 0, 0, 0) == 1, "OR5(0, 1, 0, 0, 0) failed"
    assert OR5(0, 1, 0, 0, 1) == 1, "OR5(0, 1, 0, 0, 1) failed"
    assert OR5(0, 1, 0, 1, 0) == 1, "OR5(0, 1, 0, 1, 0) failed"
    assert OR5(0, 1, 0, 1, 1) == 1, "OR5(0, 1, 0, 1, 1) failed"
    assert OR5(0, 1, 1, 0, 0) == 1, "OR5(0, 1, 1, 0, 0) failed"
    assert OR5(0, 1, 1, 0, 1) == 1, "OR5(0, 1, 1, 0, 1) failed"
    assert OR5(0, 1, 1, 1, 0) == 1, "OR5(0, 1, 1, 1, 0) failed"
    assert OR5(0, 1, 1, 1, 1) == 1, "OR5(0, 1, 1, 1, 1) failed"
    assert OR5(1, 0, 0, 0, 0) == 1, "OR5(1, 0, 0, 0, 0) failed"
    assert OR5(1, 0, 0, 0, 1) == 1, "OR5(1, 0, 0, 0, 1) failed"
    assert OR5(1, 0, 0, 1, 0) == 1, "OR5(1, 0, 0, 1, 0) failed"
    assert OR5(1, 0, 0, 1, 1) == 1, "OR5(1, 0, 0, 1, 1) failed"
    assert OR5(1, 0, 1, 0, 0) == 1, "OR5(1, 0, 1, 0, 0) failed"
    assert OR5(1, 0, 1, 0, 1) == 1, "OR5(1, 0, 1, 0, 1) failed"
    assert OR5(1, 0, 1, 1, 0) == 1, "OR5(1, 0, 1, 1, 0) failed"
    assert OR5(1, 0, 1, 1, 1) == 1, "OR5(1, 0, 1, 1, 1) failed"
    assert OR5(1, 1, 0, 0, 0) == 1, "OR5(1, 1, 0, 0, 0) failed"
    assert OR5(1, 1, 0, 0, 1) == 1, "OR5(1, 1, 0, 0, 1) failed"
    assert OR5(1, 1, 0, 1, 0) == 1, "OR5(1, 1, 0, 1, 0) failed"
    assert OR5(1, 1, 0, 1, 1) == 1, "OR5(1, 1, 0, 1, 1) failed"
    assert OR5(1, 1, 1, 0, 0) == 1, "OR5(1, 1, 1, 0, 0) failed"
    assert OR5(1, 1, 1, 0, 1) == 1, "OR5(1, 1, 1, 0, 1) failed"
    assert OR5(1, 1, 1, 1, 0) == 1, "OR5(1, 1, 1, 1, 0) failed"
    assert OR5(1, 1, 1, 1, 1) == 1, "OR5(1, 1, 1, 1, 1) failed"
    print("OR5 gate passed")

    # NOR32
    assert NOR32(0x00000000) == 1, "NOR32(0) failed"
    assert NOR32(0x00000001) == 0, "NOR32 LSB=1 failed"
    assert NOR32(0x00008000) == 0, "NOR32 middle bit=1 failed"
    assert NOR32(0x80000000) == 0, "NOR32 MSB=1 failed"
    for i in range(32): assert NOR32(1 << i) == 0, f"NOR32 failed when bit {i} is 1"
    assert NOR32(0xFFFFFFFF) == 0, "NOR32(0xFFFFFFFF) failed"
    print("NOR32 gate passed")

    print("\nAll Tests Passed")


try:
    gates_tb()

except Exception as error:
    print(error)

finally:
    print("Simulation Complete")
