class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __eq__(self, other):
        return self.numerator * other.denominator == other.numerator * self.denominator


a = Fraction(1, 2)
b = Fraction(2, 4)
print(a == b)
