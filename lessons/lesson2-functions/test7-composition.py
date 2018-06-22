import operator
import functools


def composition(f, g):
    return lambda x: f(g(x))


def double(x):
    return x*2


res = composition(double, double)

# res = composition(operator.add, functools.partial(operator.add, 1))

print(res(4))


