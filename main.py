from re import I
from register import Register
from direct_register import DirectRegister
from alu import Alu
from ram import Ram
from program_counter import ProgrammCounter
from bus import Bus
from helper import array_to_decimal

import time

s = 16
class CPU:
    def __init__(self):
        self.bus = Bus(s)
        self.a_reg = DirectRegister(s, self.bus)
        self.b_reg = DirectRegister(s, self.bus)
        self.instr_reg = DirectRegister(s, self.bus)

        self.alu = Alu(s, self.bus)
        self.ram = Ram(s, self.bus)
        self.program_counter = ProgrammCounter(int(s/2), self.bus)

def bin_list(s):
    return [bit != "0" for bit in s]
        
    
if __name__ == "__main__":
    cpu = CPU()

    cpu.program_counter.jump(bin_list("00000010"))
    cpu.ram.cells[2].register_in(bin_list("1000100010011011")) 

    while True:
        # Set Memory address register to pc
        print("CO MI")
        cpu.program_counter.counter_out()
        cpu.ram.address_in()
        print(cpu.bus)

        # Put instruction from ram into instruction register
        print("RO II")
        cpu.ram.ram_out()
        cpu.instr_reg.register_in()
        
        instruction = array_to_decimal(cpu.instr_reg.data[:8])
        print(instruction)
        if instruction == 0:
            # NOP
            pass
        elif instruction == 1:
            # LDA
            pass
        elif instruction == 2:
            # LDI
            pass
        elif instruction == 3:
            # STA
            pass
        elif instruction == 4:
            # ADD
            pass
        elif instruction == 5:
            # SUB
            pass
        elif instruction == 6:
            # J
            pass
        elif instruction == 7:
            # JC
            pass
        elif instruction == 1:
            # JZ
            pass
        elif instruction == 1:
            pass


        exit(0)

