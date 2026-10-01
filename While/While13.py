try:
    A = int(input("Введите целое число A: "))
    
    if A <= 0:
        print("Число должно быть больше 0")
    else:
        K = 1
        sum = 0.0
        
        while K <= A:
            
            K += 1
            sum += 1/K
            
        
        print(f"Наименьшее K: {K}")

except ValueError:
    print("Ошибка: введено не целое число.")
