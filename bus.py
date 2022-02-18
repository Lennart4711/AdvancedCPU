class Bus:
    def __init__(self, size):
        self.size = size
        self.data = [False]*self.size
    
    def __str__(self):
        return str(self.data)

    def bus_in(self, data):
        #assert len(data) == len(self.data)
        assert type(data)==list
        self.data = [False]*(self.size-len(data)) +data

    def bus_out(self, s=False):
        if not s:
            return self.data
        return "".join("1" if i else "0" for i in self.data)