def parse_bits(string):
    bits = []
    for char in string:
        if char == '1':
            bits.append(True)
        elif char == '0':
            bits.append(False)
    return bits

def binary_to_decimal(binary):
    return int(binary,2)

def array_to_decimal(address):
    out = "".join("1" if i else "0" for i in address)
    return int(out,2)



def array_to_str(self,a):
    return "".join("1" if num else "0" for num in a)