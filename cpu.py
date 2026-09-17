class Registers:
        
    # constructeur
    def __init__(self):
        self.R0 = 0
        self.R1 = 0
        self.R2 = 0
        self.R3 = 0
        self.R4 = 0
        self.R5 = 0
        self.R6 = 0
        self.R7 = 0
        self.PC = 0
        self.SP = 0

class Flags:
    def __init__(self):
        self.Z = 0
        self.N = 0

class Cpu:
    def __init__(self):
        self.registers = Registers()
        self.flags = Flags()