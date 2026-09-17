try:
    P = float(input())
    K = 1
    run = 10.0
    S = 10.0
    while S <= 200:
        K += 1
        run += run * P / 100
        S += run
    print(K)
    print(S)
except ValueError as e:
    print(f"произошла ошибка: {e}")