class MetaNewClass(type):
    def __init__(self, name, parents, props):
        if not hasattr(self, 'children'):
            self.children = {}
        else:
            self.children[name] = self



class NewClass(metaclass=MetaNewClass):
    pass

class B(NewClass):
    pass

class C(B):
    pass


print(NewClass.children)

