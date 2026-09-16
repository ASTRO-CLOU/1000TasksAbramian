X = float(input())
N = int(input())
s = 1.0 + X / 2
term = X / 2
for i in range(2, N + 1):
    term *= -X * (2 * i - 3) / (2 * i)
    s += term
print(s)