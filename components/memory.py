class Memory:
    def __init__(self):
        self.memory = {}


    # Load Dictionary of instructions into memory
    def load_program(self, program):
        self.memory.update(program)


    def access(self, address, memRead, memWrite, data):
        if memRead:
            return self.memory.get(address,0)

        if memWrite:
            self.memory[address] = data & 0xFFFFFFFF

        return 0