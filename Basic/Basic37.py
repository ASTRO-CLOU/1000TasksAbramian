V1 = float(input("Скорость первого авто V1: "))
V2 = float(input("Скорость второго авто V2: "))
S = float(input("Начальное расстояние S: "))
T = float(input("Время T: "))

total_S = abs(S - (V1 + V2) * T)

print(total_S)