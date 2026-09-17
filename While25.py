try:
    N = int(input())
    F1 = 1
    F2 = 1
    while F2 <= N:
        F = F1 + F2
        F1 = F2
        F2 = F
    print(F2)
except ValueError as e:
    print(f"произошла ошибка: {e}")