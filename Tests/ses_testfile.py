# Looks one file higher so python can run these files
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

# Start of testbench
from components.ses import *


def helpers_tb():
    print("Running Helpers Testbench...\n")

    # Sign Extend
    assert sign_extend(0x0000) == 0x00000000, "sign_extend(0) failed"
    assert sign_extend(0x00FF) == 0x000000FF, "sign_extend(positive) failed"
    assert sign_extend(0x7FFF) == 0x00007FFF, "sign_extend(max positive) failed"
    assert sign_extend(0x8000) == 0xFFFF8000, "sign_extend(min negative) failed"
    assert sign_extend(0xFFFF) == 0xFFFFFFFF, "sign_extend(-1) failed"
    print("sign_extend passed")

    # Zero Extend
    assert zero_extend(0x0000) == 0x00000000, "zero_extend(0) failed"
    assert zero_extend(0x000F) == 0x0000000F, "zero_extend(0x000F) failed"
    assert zero_extend(0x8000) == 0x00008000, "zero_extend(0x8000) failed"
    assert zero_extend(0xFFFF) == 0x0000FFFF, "zero_extend(0xFFFF) failed"
    print("zero_extend passed")

    # Combined Extension Unit (ext_op: 0=zero_extend, 1=sign_extend)
    assert extend_mux(0xFFFF, 0) == 0x0000FFFF, "ext_unit ORI mode failed"
    assert extend_mux(0xFFFF, 1) == 0xFFFFFFFF, "ext_unit SUBI/LW/SW mode failed"
    print("ext_unit passed")

    # Shift Left 2
    assert shift_left_2(0) == 0, "shift_left_2(0) failed"
    assert shift_left_2(1) == 4, "shift_left_2(1) failed"
    assert shift_left_2(200) == 800, "shift_left_2(200) failed"
    assert shift_left_2(0xFFFFFFFF) == 0xFFFFFFFC, "shift_left_2(-1) failed"
    print("shift_left_2 passed")

    print("\nAll Tests Passed")


try:
    helpers_tb()

except Exception as error:
    print(f"TEST FAILED: {error}")

finally:
    print("Simulation Complete")