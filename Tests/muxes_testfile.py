# Looks one file higher so python can run these files
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

# Start of testbench
from components.muxes import *


def muxes_tb():
    print("Running Muxes Testbench...\n")
    
    # Mux2
    assert mux2(0, 1, 0) == 0, "mux2 sel=0 failed"
    assert mux2(0, 1, 1) == 1, "mux2 sel=1 failed"
    assert mux2(1, 0, 0) == 1, "mux2 sel=0 failed"
    assert mux2(1, 0, 1) == 0, "mux2 sel=1 failed"
    print("mux2 passed")

    # Mux3
    assert mux3(1, 0, 0, 0) == 1, "mux3 sel=0 failed"
    assert mux3(0, 1, 0, 1) == 1, "mux3 sel=1 failed"
    assert mux3(0, 0, 1, 2) == 1, "mux3 sel=2 failed"
    assert mux3(0, 1, 1, 0) == 0, "mux3 sel=0 (zero check) failed"
    assert mux3(1, 0, 1, 1) == 0, "mux3 sel=1 (zero check) failed"
    assert mux3(1, 1, 0, 2) == 0, "mux3 sel=2 (zero check) failed"
    print("mux3 passed")

    # Mux4
    assert mux4(1, 0, 0, 0, 0) == 1, "mux4 sel=0 failed"
    assert mux4(0, 1, 0, 0, 1) == 1, "mux4 sel=1 failed"
    assert mux4(0, 0, 1, 0, 2) == 1, "mux4 sel=2 failed"
    assert mux4(0, 0, 0, 1, 3) == 1, "mux4 sel=3 failed"
    print("mux4 passed")

    # Mux5
    assert mux5(1, 0, 0, 0, 0, 0) == 1, "mux5 sel=0 failed"
    assert mux5(0, 1, 0, 0, 0, 1) == 1, "mux5 sel=1 failed"
    assert mux5(0, 0, 1, 0, 0, 2) == 1, "mux5 sel=2 failed"
    assert mux5(0, 0, 0, 1, 0, 3) == 1, "mux5 sel=3 failed"
    assert mux5(0, 0, 0, 0, 1, 4) == 1, "mux5 sel=4 failed"
    print("mux5 passed")

    print("\nAll Tests Passed")

try:
    muxes_tb()

except Exception as error:
    print(error)

finally:
    print("Simulation Complete")
