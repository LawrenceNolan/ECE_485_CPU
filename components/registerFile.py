class registerFile:
    def __init__(self):
        self.registers = [0] * 32 # $zero register

    def read(self, rs, rt):
        d1 = self.registers[rs]
        d2 = self.registers[rt]
        return d1, d2

    def write(self, register, data, reg_write):
        if reg_write and register != 0:
            self.registers[register] = data & 0xFFFFFFFF


    # Helper Method
    def print_registers(self):
        print("Register File State")
        print("Reg | Dec | Hex")
        for i in range(32):
            if self.registers != 0:
                print(f"${i:02d}: {self.registers[i]} (0x{self.registers[i]:08X})")