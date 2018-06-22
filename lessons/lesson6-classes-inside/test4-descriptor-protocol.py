# descriptor protocol
class Length:
    def __set__(self, instance, value):
        print(instance)
        instance._l = value / 100

    def __get__(self, instance, owner):
        if instance is None:
            print(owner)
        else:
            print(instance)

        return instance._l * 100


class Line:
    length = Length()

    def __init__(self):
        self._l = 0


line = Line()


line.length = 4


print(line._l)
print(line.length)


