# ... elipsis @ for numpy
import numbers


class RepresentationMixin:
    def __repr__(self):
        return "{}({})".format(
            self.__class__.__name__,
            ', '.join(["{}={}".format(name, value) for name, value in self.__dict__.items()])
        )


class Number(RepresentationMixin):
    def __init__(self, n):
        self._n = n

    def __add__(self, other):
        if isinstance(other, numbers.Number):
            return Number(self._n + other)
        elif isinstance(other, Number):
            return Number(self._n + other._n)

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        print('Iadd')
        return self.__add__(other)




# def f(): return ...
#
#
print(Number(2) + Number(3))
print(Number(3) + 1)
print(2 + Number(3))

a = Number(2)

a += 2
print(a)