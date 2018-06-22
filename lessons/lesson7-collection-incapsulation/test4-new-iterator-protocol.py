class MyCollection:
    def __init__(self, l=[]):
        self._l = list(l)  # l.copy()

    def __repr__(self):
        return repr(self._l)

    def __iter__(self):
        return MyListIterator(self._l)

    def __setitem__(self, key, value):  # l[0] = 55 - setter
        self._l[key] = value

    def __getitem__(self, item):  # l[0] - getter
        if isinstance(item, int):
            return self._l[item]
        elif isinstance(item, tuple):
            return [self._l[i] for i in item]
        elif item is ...:
            self._l.copy()

        raise IndexError


class MyListIterator:
    def __init__(self, l):
        self._l = l
        self._i = 0

    def __iter__(self):
        return self

    def __next__(self):
        print('next')
        if self._i == len(self._l):
            raise StopIteration
        self._i += 1
        return self._l[self._i - 1]


l2 = MyCollection([1, 2])

for i in l2:
    for j in l2:
        print(i, j)

print(l2)
