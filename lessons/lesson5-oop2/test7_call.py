class Scale:
    def __init__(self, k):
        self.k = k

    def __call__(self, f):
        def wrapper(x):
            return f(x) * self.k
        return wrapper


@Scale(5)
def get_area(x):
    return x*x

# class Multiplayer:
#     def __init__(self, a):
#         self.a = a
#
#     def __call__(self, *args, **kwargs):
#         return self.a * args[0]


# double = Multiplayer(2)

print(get_area(2))

# print(double(2))
# print(double(2))
