class A:
    x = 1  # static
    def f(self):
        print('A')


class B:
    def f(self):
        print('B')

a = A()
a.f()

print(vars(a))  # doesn't exist x

a.__class__ = B
a.f()
