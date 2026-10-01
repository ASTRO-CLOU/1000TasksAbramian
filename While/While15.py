try:
    P = float(input("Введите проценты: "))
    S = 1000.0
    K = 0
except ValueError:
    print("Ошибка: введено не число.")
    
if not (0<P<25):
    raise ValueError("Проценты должны быть больше нуля и меньше 25")
    
while S < 1100:
        K += 1
        S += 1000 / (100/P)
    

print(K)
print(S)


