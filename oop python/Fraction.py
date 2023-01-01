class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return str(self.numerator) + "/" + str(self.denominator)
    
    def __add__(self, other):
       return Fraction(self.numerator * other.denominator + self.denominator * other.numerator, self.denominator * other.denominator)
       
x=Fraction(3,2)
y=Fraction(2,3)
print(x+y)

