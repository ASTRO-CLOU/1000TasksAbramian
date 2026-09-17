try:
    N = int(input("Введите целое число N: "))
    
    if N <= 0:
        print("Число должно быть больше 0")
    else:
        K = 1 
        sum = 0 
        
        while sum <= N:
            
            for i in range(1, K + 1):
                sum += i
            K += 1
        
        sum -= K
        K -= 1
    
        print(f"Наибольшее K: {K}")
        print(f"Сумма: {sum}")

except ValueError:
    print("Ошибка: введено не целое число.")
