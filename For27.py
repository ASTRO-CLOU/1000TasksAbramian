X = float(input())
N = int(input())
s = X
term = X
for i in range(1, N + 1):
    term *= X * X * (2 * i - 1) / (2 * i)
    s += term / (2 * i + 1)
print(s)