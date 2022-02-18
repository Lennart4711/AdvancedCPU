from register import Register

class Ram:
    def __init__(self, size, bus):
        self.bus = bus
        self.size = size
        self.cells = [Register(self.size)]*(self.size**2)
        self.address_memory = Register(self.size)

    # takes boolean list
    def address_in(self):
        self.address_memory.register_in(self.bus.bus_out()[:int(self.size/2)])
    
    def ram_in(self):
        # Get current address from address memory
        address = int(self.address_memory.register_out(True))
        # Store data (on the bus) in the register
        self.cells[address].register_in(self.bus.bus_out())
    
    def ram_out(self):
        # Get current address from address memory
        address = int(self.address_memory.register_out(True))
        # Return data at given address
        self.bus.bus_in(self.cells[int(str(address),2)].register_out())
    
    def binary_to_decimal(binary):
        return int(binary,2)

    def array_to_decimal(address):
        out = "".join("1" if i else "0" for i in address)
        return binary_to_decimal(out)