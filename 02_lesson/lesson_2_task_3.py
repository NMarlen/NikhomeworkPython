import math


def square(side: float) -> int:

    area = side * side
    return math.ceil(area)


s = 65.3
result = square(s)
print(f"Сторона квадрата = {s}, площадь = {result}")
