import numbers

class EqMixin:
    def __eq__(self, other):
        if isinstance(other, numbers.Number):
            return self._n == other
        elif isinstance(other, Number):
            return self.__dict__ == other.__dict__
        else:
            return NotImplemented


class HashMixin:
    def __hash__(self):
        return hash(self._n)


class Number(EqMixin, HashMixin):
    def __init__(self, n):
        self._n = n


print(3 == Number(3))
#  NotImplemented type for eq
print('3' == Number(3))