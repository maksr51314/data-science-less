class Singletone:
    __obj : None
    def __new__(cls, *args, **kwargs):
        if isinstance(Singletone.__obj, cls):
            Singletone.__obj = super().__new__(cls)



s1 = Singletone()
s2 = Singletone()
