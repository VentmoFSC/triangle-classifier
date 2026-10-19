import math

def is_valid_triangle(a, b, c) -> bool:
    if a <= 0 or b <= 0 or c <= 0:
        return False
    if a + b <= c or a + c <= b or b + c <= a:
        return False
    return True

def classify_triangle(a, b, c) -> str:
    if not is_valid_triangle(a, b, c):
        return "Invalid"
    if a == b == c:
        triangle_type = "Equilateral"
    elif a == b or b == c or a == c:
        triangle_type = "Isosceles"
    else:
        triangle_type = "Scalene"

    sides = sorted ([a, b, c])
    x,y,z = sides

    if math.isclose(x**2 + y**2, z**2):
        return "Right " + triangle_type

    return triangle_type;

