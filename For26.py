X = float(input())
N = int(input())
s = 0.0
for i in range(N + 1):
    s += pow(-1, i) * pow(X, 2 * i + 1) / (2 * i + 1)
print(s)