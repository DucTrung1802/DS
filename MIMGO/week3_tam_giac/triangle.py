from math import sqrt, cos


class Triangle:
    """Define a triangle."""

    def __init__(self, a, b, c):
        """Defile a triangle with 3 edges."""
        self.a = a
        self.b = b
        self.c = c
        return self.is_triangle()

    def calculate_perimeter(self):
        return self.a + self.b + self.c

    def calculate_area(self):
        s = self.calculate_perimeter() / 2
        return sqrt(s(s - self.a)(s - self.b)(s - self.c))

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
        return self.a == self.b == self.c

    def check_isosceles_triangle(self):
        return (
            (self.a == self.b != self.c)
            or (self.a == self.b != self.c)
            or (self.b == self.c != self.a)
        )

    def calculate_cos_of_biggest_angle(self):
        

    def check_square_triangle(self):
        pass

    def check_normal_triangle(self):
        pass

    def check_obtuse_triangle(self):
        pass

    def check_triangle_type(self):
        pass
