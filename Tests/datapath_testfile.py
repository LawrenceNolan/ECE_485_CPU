import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

# Start of testbench
# Tests instructions: ori (used for setup), subi, add, sw, lw, bne
from datapath import MultiCycleDatapath

# Standard MIPS ALUControl codes
ALU_AND = 0b0000
ALU_OR  = 0b0001
ALU_ADD = 0b0010
ALU_SUB = 0b0110


def datapath_tb():
    print("Running MultiCycleDatapath Testbench...\n")

    dp = MultiCycleDatapath()

    # Exact 32-bit machine encodings matching the instruction formats
    program = {
        # 1. ori  $t0 ($8),  $zero ($0), 10   -> opcode=001101, rs=0,  rt=8,  imm=10
        0x00: 0x3408000A,
        # 2. subi $t1 ($9),  $t0 ($8),   3    -> opcode=001010, rs=8,  rt=9,  imm=3  ($9 = 7)
        0x04: 0x29090003,
        # 3. add  $t2 ($10), $t0 ($8), $t1($9)-> opcode=000000, rs=8,  rt=9,  rd=10, funct=100000 ($10 = 17)
        0x08: 0x01095020,
        # 4. sw   $t2 ($10), 100($t0 ($8))    -> opcode=101011, rs=8,  rt=10, imm=100 (Mem[110] = 17)
        0x0C: 0xAD0A0064,
        # 5. lw   $t3 ($11), 100($t0 ($8))    -> opcode=100011, rs=8,  rt=11, imm=100 ($11 = 17)
        0x10: 0x8D0B0064,
        # 6. bne  $t1 ($9),  $t2 ($10), +1    -> opcode=000101, rs=9,  rt=10, imm=1 (PC -> 0x1C)
        0x14: 0x152A0001,
    }
    dp.memory.load_program(program)

    def step(IorD=0, MemRead=0, MemWrite=0, IRWrite=0, RegDst=0, MemToReg=0,
             RegWrite=0, ALUSrcA=0, ALUSrcB=0, ExtOp=1, ALUControl=ALU_ADD,
             PCSource=0, PCWrite=0, PCWriteCond=0):
        dp.run_cycle(IorD, MemRead, MemWrite, IRWrite, RegDst, MemToReg,
                     RegWrite, ALUSrcA, ALUSrcB, ExtOp, ALUControl,
                     PCSource, PCWrite, PCWriteCond)

    # 1. ORI $t0, $zero, 10  (PC = 0x00 -> $8 = 10)
    step(IorD=0, MemRead=1, IRWrite=1, ALUSrcA=1, ALUSrcB=1, ALUControl=ALU_ADD, PCSource=0, PCWrite=1)  # IF (ALUSrcA=1 gets PC)
    step(ALUSrcA=1, ALUSrcB=3, ALUControl=ALU_ADD)                                                      # ID
    step(ALUSrcA=0, ALUSrcB=2, ExtOp=0, ALUControl=ALU_OR)                                              # EX (ALUSrcA=0 gets A | 10, zero-ext)
    step(RegDst=0, MemToReg=0, RegWrite=1)                                                              # WB ($8 = 10)

    assert dp.reg_file.read(8, 0)[0] == 10, "ORI $t0 = 10 failed"
    print("1. ORI ($t0 = 10) passed")

    # 2. SUBI $t1, $t0, 3  (PC = 0x04 -> $9 = 7)
    step(IorD=0, MemRead=1, IRWrite=1, ALUSrcA=1, ALUSrcB=1, ALUControl=ALU_ADD, PCSource=0, PCWrite=1)  # IF
    step(ALUSrcA=1, ALUSrcB=3, ALUControl=ALU_ADD)                                                      # ID
    step(ALUSrcA=0, ALUSrcB=2, ExtOp=1, ALUControl=ALU_SUB)                                             # EX (10 - 3, sign-ext)
    step(RegDst=0, MemToReg=0, RegWrite=1)                                                              # WB ($9 = 7)

    assert dp.reg_file.read(9, 0)[0] == 7, "SUBI $t1 = 7 failed"
    print("2. SUBI ($t1 = 7) passed")

    # 3. ADD $t2, $t0, $t1  (PC = 0x08 -> $10 = 17)
    step(IorD=0, MemRead=1, IRWrite=1, ALUSrcA=1, ALUSrcB=1, ALUControl=ALU_ADD, PCSource=0, PCWrite=1)  # IF
    step(ALUSrcA=1, ALUSrcB=3, ALUControl=ALU_ADD)                                                      # ID
    step(ALUSrcA=0, ALUSrcB=0, ALUControl=ALU_ADD)                                                      # EX (10 + 7)
    step(RegDst=1, MemToReg=0, RegWrite=1)                                                              # WB ($10 = 17)

    assert dp.reg_file.read(10, 0)[0] == 17, "ADD $t2 = 17 failed"
    print("3. ADD ($t2 = 17) passed")

    # 4. SW $t2, 100($t0)  (PC = 0x0C -> Mem[110] = 17)
    step(IorD=0, MemRead=1, IRWrite=1, ALUSrcA=1, ALUSrcB=1, ALUControl=ALU_ADD, PCSource=0, PCWrite=1)  # IF
    step(ALUSrcA=1, ALUSrcB=3, ALUControl=ALU_ADD)                                                      # ID
    step(ALUSrcA=0, ALUSrcB=2, ExtOp=1, ALUControl=ALU_ADD)                                             # EX (10 + 100 = 110)
    step(IorD=1, MemWrite=1)                                                                            # MEM (Mem[110] = 17)

    assert dp.memory.access(110, memRead=1, memWrite=0, data=0) == 17, "SW Mem[110] = 17 failed"
    print("4. SW (Mem[110] = 17) passed")

    # 5. LW $t3, 100($t0)  (PC = 0x10 -> $11 = 17)
    step(IorD=0, MemRead=1, IRWrite=1, ALUSrcA=1, ALUSrcB=1, ALUControl=ALU_ADD, PCSource=0, PCWrite=1)  # IF
    step(ALUSrcA=1, ALUSrcB=3, ALUControl=ALU_ADD)                                                      # ID
    step(ALUSrcA=0, ALUSrcB=2, ExtOp=1, ALUControl=ALU_ADD)                                             # EX (10 + 100 = 110)
    step(IorD=1, MemRead=1)                                                                             # MEM (MDR = Mem[110])
    step(RegDst=0, MemToReg=1, RegWrite=1)                                                              # WB ($11 = 17)

    assert dp.reg_file.read(11, 0)[0] == 17, "LW $t3 = 17 failed"
    print("5. LW ($t3 = 17) passed")

    # 6. BNE $t1, $t2, +1  (PC = 0x14 -> branches to 0x1C)
    step(IorD=0, MemRead=1, IRWrite=1, ALUSrcA=1, ALUSrcB=1, ALUControl=ALU_ADD, PCSource=0, PCWrite=1)  # IF (PC -> 0x18)
    step(ALUSrcA=1, ALUSrcB=3, ExtOp=1, ALUControl=ALU_ADD)                                             # ID (ALUOut = 0x18 + 4 = 0x1C)
    step(ALUSrcA=0, ALUSrcB=0, ALUControl=ALU_SUB, PCSource=1, PCWriteCond=1)                           # EX ($t1(7) != $t2(17) -> PC = 0x1C)

    assert dp.PC.read() == 0x1C, f"BNE failed: expected PC=0x1C, got {hex(dp.PC.read())}"
    print("6. BNE (PC -> 0x1C) passed")

    print("\nAll Tests Passed")


try:
    datapath_tb()
except Exception as error:
    print(error)
finally:
    print("Simulation Complete")