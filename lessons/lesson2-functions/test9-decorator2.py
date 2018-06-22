
def scale(scale):
    def decorator(f):
        def wrapper(x):
            print("In")
            res = f(x*scale)
            print("Out")
            return res
        return wrapper
    return decorator


# get_area = scale(20)(get_area)

@scale(3)
def get_area(x):
    return x*2


print(get_area)


# res = scale(get_area)
#
#
# print(res())





