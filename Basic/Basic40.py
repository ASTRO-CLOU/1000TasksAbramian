A1 = float(input("Введите A1: "))
B1 = float(input("Введите B1: "))
C1 = float(input("Введите C1: "))
A2 = float(input("Введите A2: "))
B2 = float(input("Введите B2: "))
C2 = float(input("Введите C2: "))

D = A1 * B2 - A2 * B1
x = (C1 * B2 - C2 * B1) / D
y = (A1 * C2 - A2 * C1) / D

print(x)
print(y)