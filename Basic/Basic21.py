import math

x1 = float(input("Введите x1: "))
y1 = float(input("Введите y1: "))
x2 = float(input("Введите x2: "))
y2 = float(input("Введите y2: "))
x3 = float(input("Введите x3: "))
y3 = float(input("Введите y3: "))

a = math.sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))
b = math.sqrt(pow(x3 - x2, 2) + pow(y3 - y2, 2))
c = math.sqrt(pow(x1 - x3, 2) + pow(y1 - y3, 2))

P = a + b + c
p = P / 2
S = math.sqrt(p * (p - a) * (p - b) * (p - c))

print(P)
print(S)