class MyCollection:
    def __init__(self, l=[]):
        self._l = list(l)  # l.copy()

    def __repr__(self):
        return repr(self._l)



l1 = MyCollection([12, 3])

print(l1)
