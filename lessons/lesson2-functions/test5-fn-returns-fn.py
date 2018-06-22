def f(a):
    def g(x):
        return x*a
    return g


res1 = f(2)
res = res1(4)
# res = res1(4)

# print(res)

a = 2


def add(x, y=a):
    return x + y


print(add(5))

a = 10

print(add(5))
