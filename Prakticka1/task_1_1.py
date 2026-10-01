import sys
import math
import random
print("Версия Python:", sys.version.split()[0], "Интерпретатор: ", sys.executable, "Количество путей пойска:", len(sys.path))

for p in sys.path[:4]:
    print("     ", p)

print("math.pi =",math.pi)
print("random.random =",random.random())

mods = sorted(sys.modules)
print("Всего загружено модулей: ",len(mods))
print("Пример: ",mods[:5])

public = [n for n in dir(math) if not n.startswith('__')]
print("Публичных имен в math: ", len(public))
print("Первые 8:", public[:8])

print("Мой __name__=", __name__)