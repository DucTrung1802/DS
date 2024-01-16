from math import sqrt


class Triangle:
    """Define a triangle."""

    def __init__(self, a, b, c):
        """Define a triangle with 3 edges."""
        self.a = a
        self.b = b
        self.c = c

    def calculate_perimeter(self):
        return self.a + self.b + self.c

    def calculate_area(self):
        s = self.calculate_perimeter() / 2
        return sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def is_triangle(self):
        if (
            (self.a + self.b > self.c)
            and (self.b + self.c > self.a)
            and (self.c + self.a > self.b)
        ):
            return True
        else:
            return False

    def check_equilateral_triangle(self):
        return self.a == self.b and self.a == self.c

    def check_isosceles_triangle(self):
        return (
            (self.a == self.b and self.a != self.c)
            or (self.a == self.c and self.a != self.b)
            or (self.b == self.c and self.b != self.a)
        )

    def calculate_cos_of_biggest_angle(self):
        if (self.a >= self.b) and (self.a >= self.c):
            return (pow(self.b, 2) + pow(self.c, 2) - pow(self.a, 2)) / (
                2 * self.b * self.c
            )
        elif (self.b >= self.a) and (self.b >= self.c):
            return (pow(self.a, 2) + pow(self.c, 2) - pow(self.b, 2)) / (
                2 * self.a * self.c
            )
        elif (self.c >= self.a) and (self.c >= self.b):
            return (pow(self.a, 2) + pow(self.b, 2) - pow(self.c, 2)) / (
                2 * self.a * self.b
            )

    def check_square_triangle(self):
        if (
            (pow(self.a, 2) == pow(self.b, 2) + pow(self.c, 2))
            or (pow(self.b, 2) == pow(self.a, 2) + pow(self.c, 2))
            or (pow(self.c, 2) == pow(self.a, 2) + pow(self.b, 2))
        ):
            return True
        return False

    def check_obtuse_triangle(self):
        if (
            (pow(self.a, 2) > pow(self.b, 2) + pow(self.c, 2))
            or (pow(self.b, 2) > pow(self.a, 2) + pow(self.c, 2))
            or (pow(self.c, 2) > pow(self.a, 2) + pow(self.b, 2))
        ):
            return True
        return False

    def check_triangle_type(self):
        if self.check_equilateral_triangle():
            return "equilateral triangle"
        elif self.check_isosceles_triangle():
            return "isosceles triangle"
        elif self.check_square_triangle():
            return "square triangle"
        elif self.check_obtuse_triangle():
            return "obtuse triangle"
        else:
            return "normal triangle"

    def check_normal_triangle(self):
        if (
            self.check_equilateral_triangle()
            or self.check_isosceles_triangle()
            or self.check_square_triangle()
            or self.check_obtuse_triangle()
        ):
            return False
        return True
