X = float(input())
N = int(input())
s = 0.0
for i in range(1, N + 1):
    s += pow(-1, i - 1) * pow(X, i) / i
print(s)