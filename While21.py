try:
    N = int(input())
    found = False
    while N > 0:
        if (N % 10) % 2 != 0:
            found = True
        N //= 10
    if found:
        print("TRUE")
    else:
        print("FALSE")
except ValueError as e:
    print(f"произошла ошибка: {e}")