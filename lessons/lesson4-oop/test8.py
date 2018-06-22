class A:
    a = 1
    def f(self):
        print(self.a)

    @classmethod
    def g(cls):
        print(cls.a)

    @staticmethod
    def h():
        print(A.a)

a = A()

a.f()

a.g()

# a.h()

A.g()

# A.h()

class B(A):
    a = 2


print(B.g())