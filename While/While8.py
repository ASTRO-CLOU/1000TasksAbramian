try:
    N = int(input("Введите целое число N: "))
    
    if N <= 0:
        print("Число должно быть больше 0")
    else:
        K = 1
        
        while pow(K, 2) <= N:

            K += 1
        
        K -= 1
            
        print(f"Наибольшее целое число которое в квадрате <= N: {K}")

except ValueError:
    print("Ошибка: введено не целое число.")
