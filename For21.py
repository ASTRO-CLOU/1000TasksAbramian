N = int(input())
s = 1.0
f = 1.0
for i in range(1, N + 1):
    f *= i
    s += 1 / f
print(s)