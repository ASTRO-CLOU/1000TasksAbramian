X = float(input("Масса шоколадных конфет X кг: "))
A = float(input("Их стоимость A руб: "))
Y = float(input("Масса ирисок Y кг: "))
B = float(input("Их стоимость B руб: "))

price_choc = A / X
price_iris = B / Y
difference = price_choc / price_iris

print(price_choc)
print(price_iris)
print(difference)