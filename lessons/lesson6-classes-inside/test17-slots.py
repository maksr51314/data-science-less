import sys


class Point:
    # __slots__ = ('x', 'y')
    def __init__(self, x, y):
        self.x, self.y = x, y


p = Point(2, 3)
p.z = 5


print(sys.getsizeof(p))
