import math
from .flat import circle_area
def sphere_volume(r): return 4 / 3 * math.pi * pow(r,3)
def cube_volume(a): return pow(a, 3)
def hemisphere_area(r):
    """Площадь полусферы: боковая поверхность + основание."""
    return 2 * math.pi * pow(r, 2) + circle_area(r)