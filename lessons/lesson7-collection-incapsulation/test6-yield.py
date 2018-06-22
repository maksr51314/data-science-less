print((x * x for x in range(10)))  # generator
print([x * x for x in range(10)])  # NON generator


#  https://docs.python.org/3.6/library/itertools.html
def f(x, y):
    if x < 0:
        return 2
    else:
        return 42


def g(l):
    return l


f(-1, g([1, 2, 23, 1, 321, 321, 3, 213, 12, 31, 23, 132, ]))


#  side effect
def g1():
    global a
    a = 5


# lazy evaluations

def inf_list():
    i = 0
    while True:
        yield i
        i += 1



l = inf_list()

# print(next(l))
# print(next(l))
# print(next(l))
# print(next(l))
# print(next(l))

for i in inf_list():
    if i * i > 100:
        break
    print(i, i * i)




import itertools

print(list(itertools.takewhile(lambda x: x*x < 100, itertools.count(0))))


l = [0, 0, 0, 1, 1, 3,3,3,3,3]

print([(k, len(list(v))) for k, v in itertools.groupby(l)])


# Coroutinos - Со програми
