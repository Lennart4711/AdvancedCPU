from helper import *

class Register:
    def __init__(self, size):
        self.size = size
        self.data = [False]*self.size

    def __str__(self):
        return str(self.data)

    def register_in(self, data):
        assert len(data) == len(self.data)
        assert type(data)==list
        self.data = data
    
    # Gives byte-string on True,
    # else list of booleans
    def register_out(self, s=False):
        if not s:
            return self.data
        return "".join("1" if i else "0" for i in self.data)