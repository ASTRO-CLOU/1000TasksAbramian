try:
    N = int(input())
    F1 = 1
    F2 = 1
    K = 2
    while F2 < N:
        F = F1 + F2
        F1 = F2
        F2 = F
        K += 1
    print(K)
except ValueError as e:
    print(f"произошла ошибка: {e}")