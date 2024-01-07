from math import sqrt


def solveQuadratic(a, b, c):
    if a == 0 and b == 0 and c == 0:
        return None
    if a == 0 and b == 0:
        return []
    if a == 0:
        return [-c / b]
    delta = b**2 - 4 * a * c
    if delta < 0:
        return []
    if delta == 0:
        return [-b / (2 * a)]
    if delta > 0:
        return [(-b - sqrt(delta)) / (2 * a), (-b + sqrt(delta)) / (2 * a)]


# print(solveQuadratic(1, 3, 2))
