from operator import xor


a = bin(5)
b = bin(6)

print(a, ' & ', b, a and b)

print(a, ' | ', b, a or b)

print(a, ' ^ ', b, bin(5 ^ 6))