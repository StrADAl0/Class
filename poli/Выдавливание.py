from math import pi


class Square:
    def __init__(self, side):
        self.area = side ** 2
    
    def extrude(self, h):
        return self.area * h


class Rectangle:
    def __init__(self, side1, side2):
        self.area = side1 * side2
    
    def extrude(self, h):
        return self.area * h 

class Triangle:
    def __init__(self, side):
        self.area = (3 ** 0.5) * (side ** 2) / 4
    
    def extrude(self, h):
        return self.area * h


class Circle:
    def __init__(self, radius):
        self.area = pi * (radius ** 2)
    
    def extrude(self, h):
        return self.area * h