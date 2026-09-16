import math
X = float(input())
N = int(input())
s = 1.0
for i in range(1, N + 1):
    s += pow(-1, i) * pow(X, 2 * i) / math.factorial(2 * i)
print(s)