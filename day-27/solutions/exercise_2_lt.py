class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __repr__(self):
        return f"{self.numerator}/{self.denominator}"

    def __lt__(self, other):
        return self.numerator * other.denominator < other.numerator * self.denominator


fractions = [Fraction(3, 4), Fraction(1, 2), Fraction(5, 8)]
print(sorted(fractions))
