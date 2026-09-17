try:
    N = int(input())
    while N > 0:
        print(N % 10)
        N //= 10
except ValueError as e:
    print(f"произошла ошибка: {e}")