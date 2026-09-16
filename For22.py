X = float(input())
N = int(input())
s = 1.0
term = 1.0
for i in range(1, N + 1):
    term *= X / i
    s += term
print(s)