import math

a = float(input("Введите катет a: "))
b = float(input("Введите катет b: "))

c = math.sqrt(pow(a, 2) + pow(b, 2))
P = a + b + c

print(c)
print(P)