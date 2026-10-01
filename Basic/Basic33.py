X = float(input("Введите массу X кг: "))
A = float(input("Введите стоимость A руб: "))
Y = float(input("Введите массу Y кг: "))

price_1kg = A / X
price_Ykg = price_1kg * Y

print(price_1kg)
print(price_Ykg)