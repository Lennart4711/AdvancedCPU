from register import Register
from alu import Alu
from ram import Ram
import time

s = 8
class CPU:
    def __init__(self):
        self.bus = Register(s)
        self.a_reg = Register(s)
        self.b_reg = Register(s)
        self.alu = Alu(s)
        self.ram = Ram(s, 16)

def bin_list(s):
    return [bit != "0" for bit in s]
        
    
if __name__ == "__main__":
    cpu = CPU()
    cpu.a_reg.register_in(bin_list("00001001"))
    cpu.b_reg.register_in(bin_list("00000101"))
    cpu.ram.address_in(bin_list("00000001"))
    print(cpu.ram.address_memory.register_out())
    cpu.ram.ram_in(bin_list("10011001"))

    print(cpu.ram.ram_out()) 