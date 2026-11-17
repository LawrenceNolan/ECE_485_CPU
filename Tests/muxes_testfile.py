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

    # 32-Bit 2-to-1 Mux (mux2_32)
    # Basic selection
    assert mux2_32(0x11111111, 0x22222222, 0) == 0x11111111, "mux2_32 sel=0 failed"
    assert mux2_32(0x11111111, 0x22222222, 1) == 0x22222222, "mux2_32 sel=1 failed"

    # Full-range bit patterns (all 0s, all 1s, alternating bits)
    assert mux2_32(0x00000000, 0xFFFFFFFF, 0) == 0x00000000, "mux2_32 all-zeros sel=0 failed"
    assert mux2_32(0x00000000, 0xFFFFFFFF, 1) == 0xFFFFFFFF, "mux2_32 all-ones sel=1 failed"
    assert mux2_32(0xAAAAAAAA, 0x55555555, 0) == 0xAAAAAAAA, "mux2_32 alternating sel=0 failed"
    assert mux2_32(0xAAAAAAAA, 0x55555555, 1) == 0x55555555, "mux2_32 alternating sel=1 failed"

    # Realistic datapath case (IorD: PC=0x00000004 vs ALUOut=0x0000012C)
    assert mux2_32(4, 300, 0) == 4, "mux2_32 IorD PC select failed"
    assert mux2_32(4, 300, 1) == 300, "mux2_32 IorD ALUOut select failed"
    print("mux2_32 passed")

    # 32-Bit 4-to-1 Mux (mux4_32)
    # Basic selection across all 4 inputs
    in0, in1, in2, in3 = 0x11111111, 0x22222222, 0x33333333, 0x44444444
    assert mux4_32(in0, in1, in2, in3, 0) == 0x11111111, "mux4_32 sel=0 failed"
    assert mux4_32(in0, in1, in2, in3, 1) == 0x22222222, "mux4_32 sel=1 failed"
    assert mux4_32(in0, in1, in2, in3, 2) == 0x33333333, "mux4_32 sel=2 failed"
    assert mux4_32(in0, in1, in2, in3, 3) == 0x44444444, "mux4_32 sel=3 failed"

    # Full-range bit patterns (0s, 1s, alternating bits, MSB-only)
    p0, p1, p2, p3 = 0x00000000, 0xFFFFFFFF, 0xAAAAAAAA, 0x80000000
    assert mux4_32(p0, p1, p2, p3, 0) == 0x00000000, "mux4_32 all-zeros failed"
    assert mux4_32(p0, p1, p2, p3, 1) == 0xFFFFFFFF, "mux4_32 all-ones failed"
    assert mux4_32(p0, p1, p2, p3, 2) == 0xAAAAAAAA, "mux4_32 alternating failed"
    assert mux4_32(p0, p1, p2, p3, 3) == 0x80000000, "mux4_32 MSB-only failed"

    # Realistic ALUSrcB datapath case: (RegB=75, Const4=4, ExtImm=300, BranchOffset=800)
    assert mux4_32(75, 4, 300, 800, 0) == 75, "mux4_32 ALUSrcB RegB failed"
    assert mux4_32(75, 4, 300, 800, 1) == 4, "mux4_32 ALUSrcB Const4 failed"
    assert mux4_32(75, 4, 300, 800, 2) == 300, "mux4_32 ALUSrcB ExtImm failed"
    assert mux4_32(75, 4, 300, 800, 3) == 800, "mux4_32 ALUSrcB BranchOffset failed"
    print("mux4_32 passed")

    print("\nAll Tests Passed")

try:
    muxes_tb()

except Exception as error:
    print(error)

finally:
    print("Simulation Complete")
