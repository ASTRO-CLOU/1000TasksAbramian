try:
    eps = float(input())
    A1 = 2.0
    A2 = 2.0 + 1.0 / A1
    K = 2
    while abs(A2 - A1) >= eps:
        A1 = A2
        A2 = 2.0 + 1.0 / A1
        K += 1
    print(K)
    print(A1)
    print(A2)
except ValueError as e:
    print(f"произошла ошибка: {e}")