A = float(input())
N = int(input())
s = 1.0
p = 1.0
for i in range(1, N + 1):
    p *= A
    s += p
print(s)