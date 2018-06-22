a = 1

def f():
    a = 2
    def g():
        nonlocal a
        a = 5
    g()
    print(a)

f()

def g(a):
    def h(x):
        return x*a
    def set_a(b):
        nonlocal a
        a = b

    h.set_a = set_a
    return h


double = g(2)


double.set_a(5)

print(dir(double), double(2))
