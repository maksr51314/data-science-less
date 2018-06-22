import numbers


class RepresentationMixin:
    def __repr__(self):
        return "{}({})".format(
            self.__class__.__name__,
            ', '.join(["{}={}".format(name, value) for name, value in self.__dict__.items()])
        )




class My_type():
    def __init__(self, type):
        self.type = type
        self.type_dic = {
            'm' : 1000,
            'mm' : 1
        }


    def getCoef(self):
        return self.type_dic[self.type]


class Shape(RepresentationMixin):
    def __init__(self, a, type):
        self._n = a
        self.type = My_type(type)


    def __add__(self, other):
        if isinstance(other, Shape):
            return self._n + other._n * other.type.getCoef()

    def __(self, other):
        if isinstance(other, Shape):
            return self._n + other._n * other.type.getCoef()

    def __add__(self, other):
        if isinstance(other, Shape):
            return self._n + other._n * other.type.getCoef()

        #     return Shape(self._n + other)
        # elif isinstance(other, Number):
            # return Shape(self._n + other._n)


a = Shape(2, 'mm')
b = Shape(3, 'm')
print(a + b)


a = Shape(3, 'm')
b = Shape(2, 'mm')
print(a + b)
