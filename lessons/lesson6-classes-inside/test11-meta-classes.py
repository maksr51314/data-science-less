class myMetaClass(type):
    def __new__(cls, name, parents, props):
        new_props = {}
        for name, value in props.items():
            if not name.startswith('unused_'):
                new_props[name] = value
        return type.__new__(cls, name, parents, new_props)


class myClass(metaclass=myMetaClass):
    unused_a = 5
    a = 2

class B(myClass):
    unused_b = 5
    b = 2

print(dir(myClass))
print(dir(B))



print(myClass.__class__)

A = type('A', (object,), {'a': 1})
print(A.__class__)

