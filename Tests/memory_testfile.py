# Looks one file higher so python can run these files
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

# Start of testbench
from components.memory import Memory


def memory_tb():
    print("Running Memory Testbench...\n")

    mem = Memory()

    # Empty Memory
    assert mem.access(0x00, memRead=1, memWrite=0, data=0) == 0, "Empty read failed"
    print("Uninitialized read passed")

    # Program load 
    program = {
        0x00: 0x00500113,  # addi x2, x0, 5
        0x04: 0x00A00193,  # addi x3, x0, 10
        0x08: 0x00310233,  # add  x4, x2, x3
    }
    mem.load_program(program)

    assert mem.access(0x00, memRead=1, memWrite=0, data=0) == 0x00500113, "Read addr 0x00 failed"
    assert mem.access(0x04, memRead=1, memWrite=0, data=0) == 0x00A00193, "Read addr 0x04 failed"
    assert mem.access(0x08, memRead=1, memWrite=0, data=0) == 0x00310233, "Read addr 0x08 failed"
    print("load_program & instruction fetch passed")

    # Read and write
    write_ret = mem.access(0x100, memRead=0, memWrite=1, data=0x12345678)
    assert write_ret == 0, "Write should return 0"
    assert mem.access(0x100, memRead=1, memWrite=0, data=0) == 0x12345678, "Read back written data failed"
    print("Data write & readback passed")

    # Over 32 bit
    mem.access(0x104, memRead=0, memWrite=1, data=0x1DEADBEEF)
    assert mem.access(0x104, memRead=1, memWrite=0, data=0) == 0xDEADBEEF, "32-bit mask failed"
    print("32-bit masking passed")

    # Idle (No read or write)
    idle_ret = mem.access(0x100, memRead=0, memWrite=0, data=0xFFFFFFFF)
    assert idle_ret == 0, "Idle read should return 0"
    assert mem.access(0x100, memRead=1, memWrite=0, data=0) == 0x12345678, "Idle state overwrote memory!"
    print("Idle state check passed")

    print("\nAll Tests Passed")

try:
    memory_tb()

except Exception as error:
    print(error)

finally:
    print("Simulation Complete")