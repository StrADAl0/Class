from math import pi


class SquareIntoCircle:
    def __init__(self, side):
        self.radius = round(2 * side / pi, 3)
    
    def size(self):
        return self.radius
    
    def area(self):
        return round(pi * (self.radius ** 2), 3)


class CircleIntoSquare:
    def __init__(self, radius):
        self.side = round(pi * radius / 2, 3)
    
    def size(self):
        return self.side
    
    def area(self):
        return round(self.side ** 2, 3)
