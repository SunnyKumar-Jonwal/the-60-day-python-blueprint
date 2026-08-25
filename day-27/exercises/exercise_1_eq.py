class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    # TODO: add __eq__ that compares self and other by cross multiplication:
    # self.numerator * other.denominator == other.numerator * self.denominator


a = Fraction(1, 2)
b = Fraction(2, 4)
# TODO: print(a == b)  -- should be True
