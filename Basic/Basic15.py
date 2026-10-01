import math

S = float(input("Введите площадь круга S: "))
pi = 3.14

R = math.sqrt(S / pi)
D = 2 * R
L = 2 * pi * R

print(D)
print(L)