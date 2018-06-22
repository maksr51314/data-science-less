class Simple:
    def __getattribute__(self, item):
        print('get attr', item)
    def __setattr__(self, key, value):
        print('set attr', key, value)
    def __delattr__(self, item):
        print('delete', item)


simple = Simple()

# simple.y

print(simple)