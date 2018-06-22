
def scale(f):
    def wrapper(x):
        print("In")
        res = f(x*10)
        print("Out")
        return res
    return wrapper


# get_area = scale(get_area)

@scale
def get_area(x):
    return x*x


print(get_area(2))


# res = scale(get_area)
#
#
# print(res())





