N = int(input())
s = 0
for i in range(N, 2 * N + 1):
    s += pow(i, 2)
print(s)