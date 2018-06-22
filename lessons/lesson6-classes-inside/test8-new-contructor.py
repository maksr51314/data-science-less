class A:
    def __new__(cls, *args, **kwargs):
        self = super().__new__(cls)

        print('new', self, *args, **kwargs)
        return self

    # def __new__(cls, *args, **kwargs):
    #     return 42

    def __init__(self, a):
        print('init', self, a)


a = A(222)

print(a)

