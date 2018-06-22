class Table:
    def __init__(self):
        self.aaa = 11
        self.__bbb = 22


table = Table()

print(vars(table))

print(table.aaa)
# print(table.__bbb)


class A:
    def __init__(self):
        self.x = 5

    def _my_private_method(self):
        self.y = 3

    def f(self):
        self.x = 2
        # self._my_private_method()
    def __repr__(self):
        return "Triangle, {}, {}, {}".format(self.a, self.b, self.c)




class B:
    pass


b = B()
A.f(b)
print(b.x)

a = A()

print(a)
# print(b.y)
