from register import Register
from alu import Alu
import time

s = 8
class CPU:
    def __init__(self):
        self.bus = Register(s)
        self.a_reg = Register(s)
        self.b_reg = Register(s)
        self.alu = Alu(s)

def bin_list(s):
    return [bit != "0" for bit in s]
        
    
if __name__ == "__main__":
    cpu = CPU()
    cpu.a_reg.register_in(bin_list("00000000"))
    cpu.b_reg.register_in(bin_list("00000000"))

    print(cpu.a_reg)
    print(cpu.b_reg)
    print(cpu.alu.alu_out(cpu.a_reg.register_out(), cpu.b_reg.register_out(), True), cpu.alu.carry)



