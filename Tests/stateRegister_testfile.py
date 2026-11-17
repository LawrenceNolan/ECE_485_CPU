# Looks one file higher so python can run these files
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from components.StateRegister import StateRegister, PCRegister


def state_registers_tb():
    print("Running State & PC Register Testbench...\n")

    # Init
    ir = StateRegister()
    assert ir.read() == 0, "Default StateRegister should initialize to 0"

    # Custom Value
    mdr = StateRegister(initial_value=0xABCD1234)
    assert mdr.read() == 0xABCD1234, "Custom initial_value failed"

    # Read and Write
    ir.write(0x00500113)
    assert ir.read() == 0x00500113, "StateRegister write/read failed"

    # bit Masking
    ir.write(0x1DEADBEEF)
    assert ir.read() == 0xDEADBEEF, "32-bit masking failed"
    print("StateRegister passed")

    # Default and custom
    pc_default = PCRegister()
    assert pc_default.read() == 0, "Default PCRegister should initialize to 0"

    pc = PCRegister(0x00400000)
    assert pc.read() == 0x00400000, "Custom PCRegister initialization failed"

    # Increment
    pc.write(pc.read() + 4)
    assert pc.read() == 0x00400004, "PC + 4 update failed"

    pc.write(0xFFFFFFFF + 4)
    assert pc.read() == 0x00000003, "PC 32-bit wrap-around masking failed"
    print("PCRegister passed")

    print("\nAll Tests Passed")


try:
    state_registers_tb()

except Exception as error:
    print(f"TEST FAILED: {error}")

finally:
    print("Simulation Complete")