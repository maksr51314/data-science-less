class RepresentationMixin:
    def __repr__(self):
        return "{}({})".format(
            self.__class__.__name__,
            ', '.join(["{}={}".format(name, value) for name, value in self.__dict__.items()])
        )


class Person(RepresentationMixin):
    def __init__(self, name, age):
        self.name, self.age = name, age


class EqMixin:
    def __eq__(self, other):
        return self.__dict__ == other.__dict__


class HashMixin:
    def __hash__(self):
        return hash(self._n)


class Number(RepresentationMixin, EqMixin, HashMixin):
    def __init__(self, n):
        self._n = n


dict1 = {}
dict1[Number(3)] = 5

person = Person('max', 5)

num = Number(22222)

print(Number(2) is Number(2))
print(Number(2) == Number(2))

print(repr(person), repr(num))

l = [Number(1), Number(2), Number(3)]
print(l.index(Number(3)))