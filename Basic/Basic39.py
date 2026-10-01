import math

A = float(input("Введите A: "))
B = float(input("Введите B: "))
C = float(input("Введите C: "))

D = pow(B, 2) - (4 * A * C)

x1 = (-B + math.sqrt(D)) / (2 * A)
x2 = (-B - math.sqrt(D)) / (2 * A)

if x1 < x2:
    print(x1)
    print(x2)
else:
    print(x2)
    print(x1)