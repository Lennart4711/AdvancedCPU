class Adder:
    def __init__(self,size):
        self.size = size

    # Adds contents of a and b register
    # c is carry bit
    def adder_out(self,a,b,c):
        sum = bin(int(self.array_to_str(a), 2) + (int(self.array_to_str(b), 2) + int(c)))
        if len(sum[2:]) <= len(a):
            return sum[2:], 0
        return sum[3:], sum[2]

    def array_to_str(self,a):
        return "".join("1" if num else "0" for num in a)