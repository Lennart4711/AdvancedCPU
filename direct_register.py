from helper import *
# Internal Register
class DirectRegister:
    def __init__(self, size, bus):
        self.bus = bus
        self.size = size
        self.data = [False]*self.size

    def __str__(self):
        return str(self.data)

    def register_in(self):
        self.data = self.bus.bus_out()
    
    # Gives byte-string on True,
    # else list of booleans
    def register_out(self, s=False):
        if not s:
            self.bus.bus_in(self.data)
        return "".join("1" if i else "0" for i in self.data)