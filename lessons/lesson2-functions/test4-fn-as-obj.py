import functools
import operator

def f(x,cb):
    return cb()*x

def cb(a):
    return a * 4

# f(5, cb())

# res = list(map(cb ,[1,2,23]))
#
#
# res = list(filter(cb, [0,1,2,2]))


def add(a, b):
    return a + b


# res = functools.reduce(add, [1, 2, 3, 4, 5])

# res = functools.reduce(lambda a, x: a + x, [1, 2, 3, 40])

# res = [(2 * x) for x in [1, 2, 3, 4] if (x % 2)]


some_sorted_list = [(1, 2), (5, 3), (3, 4)]


some_sorted_list.sort(key=lambda x: x[0]+x[1])

print(some_sorted_list)
