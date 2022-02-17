from register import Register

class Ram:
    def __init__(self, size, storage):
        self.size = size
        self.cells = [Register(self.size)]*storage
        self.address_memory = Register(self.size)

    # takes boolean list
    def address_in(self, address):
        self.address_memory.register_in(address)
    
    def ram_in(self, data):
        # Get current address from address memory
        address = int(self.address_memory.register_out(True))
        # Store data (on the bus) in the register
        self.cells[address].register_in(data)
    
    def ram_out(self):
        # Get current address from address memory
        address = int(self.address_memory.register_out(True))
        # Return data at given address
        return self.cells[address].register_out()
    
    def binary_to_decimal(binary):
        return int(binary,2)

    def array_to_decimal(address):
        out = "".join("1" if i else "0" for i in address)
        return binary_to_decimal(out)