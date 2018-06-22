# interface inheritance ???? - JAVA


class Shape:
    def __init__(self, x, y, **kwargs):
        self.x, self.y = x, y  # kwargs.pop('x'), kwargs.pop('y')
        super().__init__(**kwargs)


class Circle(Shape):
    def __init__(self, r, **kwargs):
        self.r = r  # kwargs.pop('r')
        super().__init__(**kwargs)


class PaintedShape(Shape):
    def __init__(self, color, **kwargs):
        # print(x, y, color)
        self.color = color  # kwargs.pop('color')
        super().__init__(**kwargs)


class PaintedCircle(Circle, PaintedShape):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class PaintedCircle1(PaintedCircle, Circle):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


paintedCircle = PaintedCircle(x = 1, y = 2, r = 10, color = 'red')
paintedCircle1 = PaintedCircle1(x = 1, y = 2, r = 10, color = 'red')

print(paintedCircle.__dict__)
print(paintedCircle1.__dict__)
