class Simple:
    def __init__(self, a):
        self.a = a

    def __setattr__(self, key, value):
        if key == 'a' and hasattr(self, 'a'):
            raise AttributeError('Attr is readonly', key)
        super().__setattr__(key, value)

    def __delattr__(self, item):
        if item == 'a':
            raise AttributeError('Don\'t touch me, please !')
        super().__delattr__(item)


simple = Simple(0)

simple.a
# simple.b = 6
# del simple.a