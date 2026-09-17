try:
    N = int(input())
    count = 0
    s = 0
    while N > 0:
        count += 1
        s += N % 10
        N //= 10
    print(count)
    print(s)
except ValueError as e:
    print(f"произошла ошибка: {e}")