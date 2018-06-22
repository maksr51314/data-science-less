def add_a(cls):
    cls.a = 42
    return cls
    # def wrapper(*args):
    #     cls.a = 42
    # return wrapper


@add_a
class MyClass:
    pass


print(MyClass.a)