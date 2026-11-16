# Looks one file higher so python can run these files
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

# Start of testbench
from components.adders import *


def adders_tb():
    print("Running Adder Testbench...\n")

    # Half Adder
    assert half_adder(0, 0) == (0, 0), "half_adder(0, 0) failed"
    assert half_adder(0, 1) == (1, 0), "half_adder(0, 1) failed"
    assert half_adder(1, 0) == (1, 0), "half_adder(1, 0) failed"
    assert half_adder(1, 1) == (0, 1), "half_adder(1, 1) failed"
    print("half_adder passed")

    # Full Adder
    assert full_adder(0, 0, 0) == (0, 0), "full_adder(0, 0, 0) failed"
    assert full_adder(0, 0, 1) == (1, 0), "full_adder(0, 0, 1) failed"
    assert full_adder(0, 1, 0) == (1, 0), "full_adder(0, 1, 0) failed"
    assert full_adder(0, 1, 1) == (0, 1), "full_adder(0, 1, 1) failed"
    assert full_adder(1, 0, 0) == (1, 0), "full_adder(1, 0, 0) failed"
    assert full_adder(1, 0, 1) == (0, 1), "full_adder(1, 0, 1) failed"
    assert full_adder(1, 1, 0) == (0, 1), "full_adder(1, 1, 0) failed"
    assert full_adder(1, 1, 1) == (1, 1), "full_adder(1, 1, 1) failed"
    print("full_adder passed")

    # 32-Bit Ripple Carry Adder (RCA)
    # Basic addition
    assert adder_32(0, 0) == (0, 0), "adder32(0, 0) failed"
    assert adder_32(5, 3) == (8, 0), "adder32(5, 3) failed"
    assert adder_32(6, 7) == (13, 0), "adder32(5, 3) failed"
    assert adder_32(100, 250) == (350, 0), "adder32(100, 250) failed"

    # Carry-in check
    assert adder_32(10, 20, Cin=1) == (31, 0), "adder32 with Cin=1 failed"

    # Large numbers
    assert adder_32(0x7FFFFFFF, 1) == (0x80000000, 0), "adder32 MSB carry failed"

    # overflow 
    assert adder_32(0xFFFFFFFF, 1) == (0, 1), "adder32 max + 1 overflow failed"
    assert adder_32(0xFFFFFFFF, 0xFFFFFFFF) == (0xFFFFFFFE,1), "adder32 max + max overflow failed"
    print("adder_32 passed")

    print("\nAll Tests Passed")


try:
    adders_tb()

except Exception as error:
    print(error)

finally:
    print("Simulation Complete")


