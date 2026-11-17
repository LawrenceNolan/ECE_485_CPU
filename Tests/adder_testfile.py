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

    print("\nAll Tests Passed")


try:
    adders_tb()

except Exception as error:
    print(error)

finally:
    print("Simulation Complete")


