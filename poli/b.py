from math import pi


class Square:
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side ** 2
    
    def perimeter(self):
        return 4 * self.side
    
    def __str__(self):
        return 'Square with side {}'.format(self.side)


class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return pi * (self.radius ** 2)
    
    def perimeter(self):
        return 2 * pi * self.radius
    
    def __str__(self):
        return 'Circle with radius {}'.format(self.radius)


def compare(a, b):
    if a.area() > b.area():
        print('{} is bigger'.format(str(a)))
    elif a.area() == b.area():
        print('{} and {} are equal'.format(str(a), str(b)))
    else:
        print('{} is bigger'.format(str(b)))


a = Square(2)
b = Circle(2)
print(a.area(), b.area())
print(a.perimeter(), b.perimeter())

compare(a, b)
compare(a, a)
compare(b, b)