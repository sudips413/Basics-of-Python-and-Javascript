def add_binary(a, b):
    return bin(int(a, 2) + int(b, 2))[2:]

print(add_binary("11", "1")) # Output: "100"
print(add_binary("1010", "1011")) # Output: "10101"