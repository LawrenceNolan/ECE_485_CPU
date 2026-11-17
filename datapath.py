# Wiring everything together, manually adding control signals for each instruction
# Instruction Fetch, Register Read, Execute, Memory, Writeback
from components.gates import *
from components.muxes import *
from components.alu import alu_32bit
from components.memory import *
from components.registerFile import *
from components.ses import *

class MultiCycleDatapath:
    def __init__(self):
        self.memory = Memory()
        self.reg_file = RegisterFile()

        self.PC = PCRegister() 
        self.IR = StateRegister()
        self.MDR = StateRegister()
        self.A = StateRegister()
        self.B = StateRegister()
        self.ALUOut = StateRegister()

    def run_cycle(self, IorD, MemRead, MemWrite, IRWrite, RegDst, MemToReg, RegWrite, 
                  ALUSrcA, ALUSrcB, ExtOp, ALUControl, PCSource, PCWrite, PCWriteCond):

        # Read Current State
        PC = self.PC.read()
        IR = self.IR.read()
        MDR = self.MDR.read()
        A = self.A.read()
        B = self.B.read()
        ALUOut = self.ALUOut.read()

        # 1. Instruction Fetch / # 4. Memory Write
        mem_address = mux2(IorD, PC, ALUOut)
        mem_data = self.memory.access(mem_address, MemRead, MemWrite, B)


        # 2. Instruction Decode / Register Read
        opcode = (IR >> 16) & 0x3F
        rs = (IR >> 21) & 0x1F
        rt = (IR >> 16) & 0x1F
        rd = (IR >> 11) & 0x1F
        imm16 = IR & 0xFFFF
        jump_addr = (IR & 0x03FFFFFF)

        extended_imm = extend_mux(imm16, ExtOp)
        shifted_imm = shift_left_2(extended_imm)
        shifted_jump_addr = shift_left_2(jump_addr)

        read_A, read_B = self.reg_file.read(rs, rt)


        # 3. Execute
        alu_A = mux2_32(A, PC, ALUSrcA)
        alu_B = mux4_32(B, 4, extended_imm, shifted_imm)

        alu_result, zero_flag = alu_32bit(alu_A, alu_B, NOT(alu_B), ALUControl)
        jump_pc = (PC & 0xF0000000) | shifted_jump_addr
        nextPC = mux3_32(PCSource, alu_result, ALUOut, jump_pc)
        branch = AND(PCWriteCond, zero_flag)


        # 5. Write Back
        write_reg_addr = mux2(RegDst, rt, rd)
        write_reg_data = mux2(MemToReg, ALUOut, MDR)
        self.reg_file.write(write_reg_addr, write_reg_data, RegWrite)

        # Clock Edge
        if IRWrite == 1:
            self.IR.write(mem_data)

        self.MDR.write(mem_data)
        self.A.write(read_A)
        self.B.write(read_B)
        self.ALUOut.write(alu_result)
        
        if PCWrite == 1 or branch == 1:
            self.PC.write(nextPC)
