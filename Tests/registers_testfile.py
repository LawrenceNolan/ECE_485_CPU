# Looks one file higher so python can run these files
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

# Start of testbench
from components.registerFile import registerFile


def registers_tb():
    print("Running Register File Testbench...\n")

    rf = registerFile()

    # Init
    assert rf.read(0, 1) == (0, 0), "Initial registers not 0"
    assert rf.read(15, 31) == (0, 0), "Initial registers not 0"
    print("Initial zero state passed")

    # Write/Read
    rf.write(register=8, data=42, reg_write=1)       # $t0 = 42
    rf.write(register=9, data=0x12345678, reg_write=1)  # $t1 = 0x12345678
    assert rf.read(8, 9) == (42, 0x12345678), "Write/read $8 and $9 failed"
    print("Write & dual-port read passed")

    # $zero
    # Attempting to write to register 0 must be ignored even when reg_write=1
    rf.write(register=0, data=0xFFFFFFFF, reg_write=1)
    assert rf.read(0, 8) == (0, 42), "$0 was overwritten!"
    print("$zero hardwired protection passed")

    # write
    rf.write(register=8, data=999, reg_write=0)
    assert rf.read(8, 0) == (42, 0), "Write occurred while reg_write=0!"
    print("reg_write=0 protection passed")

    # bit masking
    rf.write(register=10, data=0x1DEADBEEF, reg_write=1)
    assert rf.read(10, 0) == (0xDEADBEEF, 0), "32-bit masking failed"
    print("32-bit masking passed")

    # print 
    print()
    rf.print_registers()

    print("\nAll Tests Passed")


try:
    registers_tb()

except Exception as error:
    print(error)

finally:
    print("Simulation Complete")