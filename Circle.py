from Shape import Shape
from math import pi


class Circle(Shape):

    def __init__(self, radius):
        if self._isvalid_value(radius):
            self.radius = radius
        else:
            raise ValueError("Invalid radius")

    def area(self):
        return pi * self.radius ** 2

    def circumference(self):
        return 2 * pi * self.radius

    def perimeter(self):
        return self.circumference()
