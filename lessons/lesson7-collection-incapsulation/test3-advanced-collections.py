class MyCollection:
    def __init__(self, l=[]):
        self._l = list(l)  # l.copy()

    def __repr__(self):
        return repr(self._l)

    def __len__(self):
        return len(self._l)

    def add(self, other):
        self._l.append(other)

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

    def __contains__(self, item):
        print('contains')
        return item in self._l

        # print(item)
        # return self._l[item]


l1 = MyCollection([12, 3, 3, 4, 5, 5])

l1.add(44)

len(l1)

l1[0] = 55

# l1[1:2]  # slice(1, 2, None)
#
l1[1, 2, 3]  # (1,2,3)

# l1[...]  # Ellipsis

for i in l1:
    print(i)

print(5 in l1)
