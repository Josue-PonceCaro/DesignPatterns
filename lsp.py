# 3. Liskov Substitution Principle
class Rectangle:
    def __init__(self, width, height):
        self._height = height
        self._width = width

    @property
    def area(self):
        return self._width * self._height

    def __str__(self):
        return f'Width: {self.width}, height: {self.height}'

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value


class Square(Rectangle):
    def __init__(self, size):
        Rectangle.__init__(self, size, size)

    @Rectangle.width.setter
    def width(self, value):
        self._width = self._height = value

    @Rectangle.height.setter
    def height(self, value):
        self._width = self._height = value


def use_it(rc,w):
    w = 10
    w = rc.width
    rc.height = 10  # unpleasant side effect
    expected = int(w * 10)
    expected2 = int(rc.width * 10)
    print(f'Expected an area of {expected}, expected 2 {expected2}, got {rc.area}')

w = 1
rc = Rectangle(2, 3)
use_it(rc,w)
print(w)
sq = Square(5)
use_it(sq,w)
print(sq.height)
