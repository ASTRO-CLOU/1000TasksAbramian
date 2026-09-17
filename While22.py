try:
    N = int(input())
    d = 2
    is_prime = True
    while d * d <= N:
        if N % d == 0:
            is_prime = False
        d += 1
    if is_prime and N > 1:
        print("TRUE")
    else:
        print("FALSE")
except ValueError as e:
    print(f"произошла ошибка: {e}")