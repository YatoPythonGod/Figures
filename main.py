from Circle import Circle
from Rectangle import Rectangle
from Square import Square
from Triangle import Triangle

figures = [Circle(5), Rectangle(5, 10), Square(10), Triangle(3, 4, 5)]

for figure in figures:
    print(f"{type(figure).__name__}:\nperimeter - {figure.perimeter()}\narea - {figure.area()}\n")
