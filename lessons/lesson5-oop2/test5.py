import functools
import numbers

class RepresentationMixin:
    def __repr__(self):
        return "{}({})".format(
            self.__class__.__name__,
            ', '.join(["{}={}".format(name, value) for name, value in self.__dict__.items()])
        )

# class EqMixin:
#     def __eq__(self, other):
#         if isinstance(other, numbers.Number):
#             return self._n == other
#         elif isinstance(other, Number):
#             return self.__dict__ == other.__dict__
#         else:
#             return NotImplemented


class LessThenMixin:
    def __lt__(self, other):
        return self._n < other._n

# class HashMixin:
#     def __hash__(self):
#         return hash(self._n)
#


@functools.total_ordering
class Number(RepresentationMixin):
    def __init__(self, n):
        self._n = n


l = [Number(1),Number(1), Number(2), Number(3)]

l.sort()

print(l)
#  NotImplemented type for eq
