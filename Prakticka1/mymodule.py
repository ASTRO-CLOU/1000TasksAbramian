import math
PI = math.pi
VERSION = "1.0.0"
_secret = "это скрытая константа"

def circle_area(r): return PI * pow(r, 2)
def circle_len(r): return PI * 2 * r
def _helper(): return PI / 2

if __name__ == '__main__':
    print(f"[{VERSION}] самопроверка mymodule:")
    print(" S(r=2) =", circle_area(2))
    print(" L(r=2) =", circle_len(2))