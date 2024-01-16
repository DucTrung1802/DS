class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise Exception("No denominators equal to 0")
        self.numerator = numerator
        self.denominator = denominator
        self.compact()

    def show(self):
        print(self.numerator, "/", self.denominator)

    def compact(self):
        if self.numerator > self.denominator:
            for i in reversed(range(2, int(self.denominator) + 1)):
                if (self.numerator % i == 0) and (self.denominator % i == 0):
                    self.numerator /= i
                    self.denominator /= i

    def add(self, fraction2):
        self.numerator = (
            self.numerator * fraction2.denominator
            + self.denominator * fraction2.numerator
        )
        self.denominator *= fraction2.denominator
        self.compact()

    def sub(self, fraction2):
        self.numerator = (
            self.numerator * fraction2.denominator
            - self.denominator * fraction2.numerator
        )
        self.denominator *= fraction2.denominator
        self.compact()

    def mul(self, fraction2):
        self.numerator *= fraction2.numerator
        self.denominator *= fraction2.denominator
        self.compact()

    def truediv(self, fraction2):
        if fraction2.numerator == 0:
            raise Exception("Divide by Zero")
        self.numerator *= fraction2.denominator
        self.denominator *= fraction2.numerator
        self.compact()


# myfrac1 = Fraction(19, 12)
# myfrac2 = Fraction(3, 4)
# myfrac1.add(myfrac2)
# myfrac1.show()
# myfrac1.sub(myfrac2)
# myfrac1.show()
# myfrac1.mul(myfrac2)
# myfrac1.show()
# myfrac1.truediv(myfrac2)
# myfrac1.show()