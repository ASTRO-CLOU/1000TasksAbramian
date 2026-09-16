N = int(input())
K = int(input())
count = 0
while N >= K:
    N -= K
    count += 1
print(count)
print(N)