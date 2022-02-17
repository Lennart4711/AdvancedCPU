from register import Register
from alu import Alu
from ram import Ram
from program_counter import ProgrammCounter
import time

s = 8
class CPU:
    def __init__(self):
        self.bus = Register(s)
        self.a_reg = Register(s)
        self.b_reg = Register(s)
        self.alu = Alu(s)
        self.ram = Ram(s, 16)
        self.program_counter = ProgrammCounter(s)

def bin_list(s):
    return [bit != "0" for bit in s]
        
    
if __name__ == "__main__":
    cpu = CPU()
    cpu.a_reg.register_in(bin_list("00001001"))
    cpu.b_reg.register_in(bin_list("00000101"))

    print(cpu.program_counter.counter_out())
    print(cpu.program_counter.count_enable())
    print(cpu.program_counter.counter_out())
    print(cpu.program_counter.count_enable())
    print(cpu.program_counter.counter_out())
    print(cpu.program_counter.count_enable())
    print(cpu.program_counter.counter_out())
    
    print(cpu.program_counter.jump(bin_list("00000001")))
    print(cpu.program_counter.counter_out())
    