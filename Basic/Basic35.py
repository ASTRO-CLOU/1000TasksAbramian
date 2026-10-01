V = float(input("Скорость лодки V: "))
U = float(input("Скорость течения U: "))
T1 = float(input("Время по озеру T1: "))
T2 = float(input("Время против течения T2: "))

S = (V * T1) + ((V - U) * T2)

print(S)