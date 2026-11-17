class StateRegister:
    def __init__(self, initial_value=0):
        self.value = initial_value

    def read(self):
        return self.value

    def write(self, new_value):
        self.value = new_value & 0xFFFFFFFF


class PCRegister(StateRegister):
    def __init__(self, inital_value=0):
        super().__init__(inital_value)