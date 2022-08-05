from assembler import ram

s = 16


def int_to_bin(n: int) -> str:
    # Convert integer to binary string with n bits
    # use twos complement if n is negative
    if n < 0:
        return bin(n + 2**s)[2:].zfill(s)
    else:
        return bin(n)[2:].zfill(s)

def bin_to_int(n: str) -> int:
    # Convert binary string to integer
    return int(n, 2)


class Bus:
    def __init__(self, size):
        self.size = size
        self.value = "0" * size
        
    def set_value(self, value):
        assert len(value) == self.size 
        assert type(value) == str
        self.value = value
    def get_value(self):
        return self.value
        

class Register:
    def __init__(self, size, bus):
        self.value = "0"*size
        self.size = size
        self.bus = bus
        
    def register_out(self):
        self.bus.set_value(self.value)
    
    def register_in(self):
        self.value = self.bus.get_value()


class MAR:
    def __init__(self, size, bus):
        self.size = size
        self.bus = bus
        self.value = "0" * int(self.size/2)
    
    def mar_in(self):
        if len(self.bus.get_value()[int(self.size/2):]) == self.size:
            ("mar in error")
        self.value = self.bus.get_value()[int(self.size/2):]
        
    def get_value(self):
        return self.value
        
class RAM:
    def __init__(self, size, bus):
        # memory addresss register
        self.half = int(size/2)
        self.cells = [Register(size, bus) for _ in range((2**self.half))]
        self.bus = bus
    
    def ram_in(self, mar: MAR):
        self.cells[bin_to_int(mar.get_value())].value = self.bus.get_value()
        
    def ram_out(self, mar: MAR):
        self.cells[bin_to_int(mar.get_value())].register_out()
        
class ProgramCounter():
    def __init__(self, size, bus):
        self.value = "0" * int(size/2)
        self.size = size
        self.bus = bus
    
    def counter_out(self):
        self.bus.set_value(int_to_bin(bin_to_int(self.value)))
    
    def jump(self):
        self.value = self.bus.get_value()[int(self.size/2):]
        
    def increment(self):
        if bin_to_int(self.value)+1 == 2**int(self.size/2):
            self.value = "0" * int(self.size/2)
            assert False, "Program counter overflow" # Remove later
        else:
            self.value = int_to_bin(bin_to_int(self.value) + 1)
            
class Flags:
    # value[0] = carry flag
    # value[1] = zero flag
    def __init__(self):
        self.carry = False
        self.zero = False
    
    def set_carry(self, value):
        (f"set carry to {value}")
        self.carry = value
    
    def set_zero(self, value):
        (f"set zero to {value}")
        self.zero = value


class ALU:
    def __init__(self, size, bus, a, b, flags):
        self.size = size
        self.bus = bus
        self.a = a
        self.b = b
        self.value = "0" * self.size
        self.flags = flags
        
    def sum_out(self, subtract=False):
        # A 16 bit alu
        a = self.a.value
        b = self.b.value
        # if subtract is true, make twos complement of b
        if subtract:
            # 1101 -> 0010 -> +1 -> 0011
            b = ['0' if x == '1' else '1' for x in b]
            b = ''.join(b)
            b = int_to_bin(bin_to_int(b) + 1)
        # add a and b
        self.value = int_to_bin(bin_to_int(a) + bin_to_int(b))
        # if the result is greater than 16 bits, set carry flag
        if len(self.value) > self.size:
            self.flags.set_carry(True)
            self.value = self.value[1:]
        # if len(self.value) > self.size, delete the first bit
        if len(self.value) > self.size:
            self.value = self.value[1:]
        # if result is zero, set zero flag
        (bin_to_int(self.value))
        if bin_to_int(self.value) == 0:
            self.flags.set_zero(True)
        else:
            self.flags.set_zero(False)
      
        self.bus.set_value(self.value)
        
        
        
        
class CPU:
    def __init__(self):
        self.bus = Bus(s)
        self.mar = MAR(s, self.bus)
        self.ram = RAM(s, self.bus)
        self.a_reg = Register(s, self.bus)
        self.b_reg = Register(s, self.bus)
        self.program_counter = ProgramCounter(s, self.bus)
        self.instr_reg = Register(s, self.bus)
        self.flags = Flags()
        self.alu = ALU(s, self.bus, self.a_reg, self.b_reg ,self.flags)
        
    def loop(self):
        # Counter out, mar in
        self.program_counter.counter_out()
        self.mar.mar_in()
        #(f"CO MI : {bin_to_int(self.bus.get_value())} ")
        
        # Ram out, instr reg in
        #("RO II")
        self.ram.ram_out(self.bus)
        self.instr_reg.register_in()
        #("CE")
        self.program_counter.increment()
        
        instruction = bin_to_int(self.instr_reg.value[:int(s/2)])
        address = bin_to_int(self.instr_reg.value[int(s/2):])
        # Decode and execute instruction        
        if instruction == 0:
            # NOP
            pass
        elif instruction == 1:
            # LDA
            self.bus.set_value(int_to_bin(address))
            self.mar.mar_in()
            self.ram.ram_out(self.mar)
            self.a_reg.register_in()
        elif instruction == 2:
            # ADD
            self.bus.set_value(int_to_bin(address))
            self.mar.mar_in()
            self.ram.ram_out(self.mar)
            self.b_reg.register_in()
            self.alu.sum_out()
            self.a_reg.register_in()
        elif instruction == 3:
            # SUB
            self.bus.set_value(int_to_bin(address))
            self.mar.mar_in()
            self.ram.ram_out(self.mar)
            self.b_reg.register_in()
            self.alu.sum_out(subtract=True)
            self.a_reg.register_in()
        elif instruction == 4:
            # STA
            self.bus.set_value(int_to_bin(address))
            self.mar.mar_in()            
            self.a_reg.register_out()          
            self.ram.ram_in(self.mar)
        elif instruction == 5:
            # LDI
            self.bus.set_value(int_to_bin(address))
            self.a_reg.register_in()
        elif instruction == 6:
            # JMPs
            self.bus.set_value(int_to_bin(address))
            self.program_counter.jump()
        elif instruction == 7:
            # JC
            if self.flags.carry:
                self.bus.set_value(int_to_bin(address))
                self.program_counter.jump()
        elif instruction == 8:
            # JZ
            if self.flags.zero:
                self.bus.set_value(int_to_bin(address))
                self.program_counter.jump()
        elif instruction == 9:
            # JNC
            if not self.flags.carry:
                self.bus.set_value(int_to_bin(address))
                self.program_counter.jump()
        elif instruction == 10:
            # JNZs
            if not self.flags.zero:
                self.bus.set_value(int_to_bin(address))
                self.program_counter.jump()
        elif instruction == 11:
            # ADI
            self.bus.set_value(int_to_bin(address))
            self.b_reg.register_in()
            self.alu.sum_out()
            self.a_reg.register_in()
        elif instruction == 12:
            # SBI
            self.bus.set_value(int_to_bin(address))
            self.b_reg.register_in()
            self.alu.sum_out(subtract=True)
            self.a_reg.register_in()
        elif instruction == 13:
            # STI
            self.bus.set_value(int_to_bin(address))
            self.mar.mar_in()
            self.a_reg.register_out()
            self.ram.ram_in(self.mar)
        elif instruction == 254:
            # OUT
            print(self.a_reg.value, bin_to_int(self.a_reg.value))
        elif instruction == 255:
            # HALT
            exit()
            
def value(n):
    s = 8
    if n < 0:
        return bin(n + 2**s)[2:].zfill(s)
    else:
        return bin(n)[2:].zfill(s)
        
if __name__ == '__main__':
    cpu = CPU()
    for i in range(256):
        cpu.ram.cells[i].value = ram[i]
    
    
    
    while True:
        cpu.loop()
        #(cpu.a_reg.value)