from adder import Adder

class Alu:
    def __init__(self, size):
        self.size = size
        self.carry = False
        self.adder = Adder(self.size)

    def array_to_str(self,a):
        return "".join("1" if num else "0" for num in a)

    def alu_out(self, a, b, sub=False):
        if sub:
            b = [not bit for bit in b]
            print(b,"b")
        out, self.carry = self.adder.adder_out(a,b,sub)
        # Fill number with missing lead zeros
        out = "0"*(self.size-len(out))+out
        # Convert to list 0->False, 1->True
        return [bit != "0" for bit in out]
        

