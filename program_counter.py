from register import Register
from adder import Adder

class ProgrammCounter:
    def __init__(self, size, bus):
        self.bus = bus
        self.size = size
        self.counter = Register(self.size)
        self.adder = Adder(self.size)

    def jump(self, address):
        self.counter.register_in(address)
    
    def counter_out(self):
        self.bus.bus_in(self.counter.register_out())

    def count_enable(self):
        out = self.adder.adder_out(self.counter.register_out(), [False]*8,True)
        new = "0"*(self.size-len(out[0]))+out[0]
        self.counter.register_in(self.bin_list(new))

    def bin_list(self,s):
        return [bit != "0" for bit in s]