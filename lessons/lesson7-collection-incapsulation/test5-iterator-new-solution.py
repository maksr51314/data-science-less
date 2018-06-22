class MyCollection:
    def __init__(self, l=[]):
        self._l = list(l)  # l.copy()

    def __repr__(self):
        return repr(self._l)

    # def __iter__(self):
    #     return iter(self._l)

    def __iter__(self):
        for i in self._l:
            yield i


def f():
    for i in range(5):
        yield i
        print('I m here')


collection = MyCollection([12,2,3])

g = f()

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))





# for i in collection:
#     for j in collection:
#         print(i, j)

# print(collection)