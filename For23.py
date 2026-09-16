import math
X = float(input())
N = int(input())
s = X
for i in range(1, N + 1):
    s += pow(-1, i) * pow(X, 2 * i + 1) / math.factorial(2 * i + 1)
print(s)