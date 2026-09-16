N = int(input())
s = 0.0
f = 1.0
for i in range(1, N + 1):
    f *= i
    s += f
print(s)