A = int(input())
B = int(input())
s = 0
for i in range(A, B + 1):
    s += pow(i, 2)
print(s)