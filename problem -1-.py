from math import sqrt
class ComplexNumber(object):
    def __init__(self, x=0, y=0):
        assert (type(x) == int or type(x) == float) and (type(y) == int or type(y) == float),"Bad input!"
        self.x = x
        self.y = y
    def __str__(self):
        return str(self.x) + '+'+ str(self.y) + 'j'

    def __neg__(self):
        return ComplexNumber(-self.x, -self.y)
    def conj(self):
        return ComplexNumber(self.x,-self.y)
    def norm(self):
        return str(sqrt(self.x**2+self.y**2))

    def __add__(self, other):
        real_part = self.x + other.x
        imaginary_part = self.y + other.y
        return ComplexNumber(real_part, imaginary_part)

    def __sub__(self, other):
        real_part = self.x - other.x
        imaginary_part = self.y - other.y
        return ComplexNumber(real_part, imaginary_part)

    def __mul__(self, other):
        real_part = self.x * other.x - self.y * other.y
        imaginary_part = self.x * other.y + self.y * other.x

        return ComplexNumber(real_part, imaginary_part)

    def __truediv__(self, other):
        real_part = ((self.x * other.x) + (self.y * other.y)) / ((other.x) * 2 + (other.y) * 2)
        imaginary_part = - (self.x * other.y + self.y * other.x) / ( (other.x) * 2 + (other.y) * 2)
        return ComplexNumber(real_part, imaginary_part)

r = ComplexNumber(12)
z = ComplexNumber(1.5,2)
t = ComplexNumber(2.2,3)
print(r)
print(z+t)
print(-z)
print(z*t)
print(z/t)
print(z.conj())
print(z.norm())
