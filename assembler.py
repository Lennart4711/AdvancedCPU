def int_to_bin(n: int, s: int) -> str:
    # Convert integer to binary string with n bits
    # use twos complement if n is negative
    if n < 0:
        return bin(n + 2**s)[2:].zfill(s)
    else:
        return bin(n)[2:].zfill(s)


opcodes = {
    "NOP": "00000000",
    "LDA": "00000001",
    "ADD": "00000010",
    "SUB": "00000011",
    "STA": "00000100",
    "LDI": "00000101",
    "J": "00000110",
    "JC": "00000111",
    "JZ": "00001000",
    "JNC": "00001001",
    "JNZ": "00001010",
    "ADI": "00001011",
    "SBI": "00001100",
    "STX": "00001101",
    "LDX": "00001110",
    "TXA": "00001111",
    "TAX": "00010000",
    "SAX": "00010001",
    "OUT": "11111110",
    "HLT": "11111111",
}
code = []
with open("program.asm", "r") as asm:
    for line in asm:
        code.append(line.split())

# Remove empty lines
code = [x for x in code if x]

variables = {}
# Add variables to dictionary
for line in code:
    if line[0] == "VAR":
        variables[line[1]] = int(line[2])

# Remove VAR lines
code = [x for x in code if x[0] != "VAR"]
ram = [0] * 256


for i, var in enumerate(variables):
    ram[-i - 1] = variables[var]

label_index = {}
pos = 0
for i, line in enumerate(code):
    if line[0].startswith("."):
        label_index[line[0]] = (i, pos)
        pos += 1
# remove label lines
code = [x for x in code if not x[0].startswith(".")]
for line in code:
    try:
        if line[1].isdigit():
            line[1] = int_to_bin(int(line[1]), 8)
    except IndexError:
        pass
# Replace labels with addresses
for line in code:
    try:
        if line[1] in label_index:
            line[1] = label_index[line[1]][0] - label_index[line[1]][1]
    except IndexError:
        pass


# Replace variables with addresses
for i, var in enumerate(variables):
    for line in code:
        try:
            if line[1] == var:
                line[1] = 255 - i
        except IndexError:
            pass

# Replace opcodes with binary
for line in code:
    try:
        line[0] = opcodes[line[0]]
    except KeyError:
        pass
# Convert addresses to binary
for line in code:
    try:
        if type(line[1]) == int:
            line[1] = int_to_bin(line[1], 8)
    except IndexError:
        line.append("00000000")

# Concatenate lines
for i in range(len(code)):
    ram[i] = code[i][0] + code[i][1]

for i, num in enumerate(ram):
    if type(num) == int:
        ram[i] = int_to_bin(num, 16)


for i in range(256):
    if ram[i] != "0" * 16:
        print(f"#{i} " + ram[i][:8] + "|" + ram[i][8:])

# # print last 4 ram cells
# print(ram[0:10])

# print(ram[-4:])
