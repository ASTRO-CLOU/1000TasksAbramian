try:
    N = int(input("Введите целое число N: "))
    
    if N <= 0:
        print("Число должно быть больше 0.")
    else:
        result = 1.0
        
        while N > 0:
            result *= N
            N -= 2
            
        print(f"Двойной факториал равен: {result}")

except ValueError:
    print("Ошибка: введено не целое число.")
