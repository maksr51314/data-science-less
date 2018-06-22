class MetaCall(type):
    def __call__(cls, *args, **kwargs):
        print(cls)
        self = type.__call__(cls, *args, **kwargs)
        self.a = 5
        return self


class Call(metaclass=MetaCall):
    pass


call = Call()

print(call.a)
