try:
    A = float(input())
    B = float(input())
    C = float(input())
    countA = 0
    tempA = A
    while tempA >= C:
        tempA -= C
        countA += 1
    countB = 0
    tempB = B
    while tempB >= C:
        tempB -= C
        countB += 1
    total = 0
    i = 0
    while i < countA:
        j = 0
        while j < countB:
            total += 1
            j += 1
        i += 1
    print(total)
except ValueError as e:
    print(f"произошла ошибка: {e}")