class A:
    def __init__(self):
        self.__a = 1
    def f(self):
        return self.__a


a = A()

print(vars(a))

class B(A):
    def __init__(self):
        super().__init__()
        self.__a = 2

b = B()

print(b.f())