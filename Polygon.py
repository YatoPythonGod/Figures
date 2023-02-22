from abc import ABC
from Shape import Shape


class Polygon(Shape, ABC):
    def __init__(self, sides: list):
        if all(map(self._isvalid_value, sides)):
            self.sides = sides
        else:
            raise ValueError("Invalid sides")

    def perimeter(self):
        return sum(self.sides)
