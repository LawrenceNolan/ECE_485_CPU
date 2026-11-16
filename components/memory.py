class Memory:
    def __init__(self):
        self.memory = {}

    def read(self, address, memRead):
        if memRead:
            return self.memory.get(address,0)
        return 0

    def write(self, address, data, memWrite):
        if memWrite:
            self.memory[address] = data & 0xFFFFFFFF