try:
    A = int(input())
    B = int(input())
    while B != 0:
        rem = A % B
        A = B
        B = rem
    print(A)
except ValueError as e:
    print(f"произошла ошибка: {e}")