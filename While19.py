try:
    N = int(input())
    res = 0
    while N > 0:
        res = res * 10 + N % 10
        N //= 10
    print(res)
except ValueError as e:
    print(f"произошла ошибка: {e}")