N = int(input())
p = 1.0
for i in range(1, N + 1):
    p *= (1 + i / 10)
print(p)