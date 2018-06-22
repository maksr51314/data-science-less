from Car import Car


class Audi(Car):
    def __init__(self, *args):
        Car.__init__(self, *args)
        # super().__init__()
        self.lll = 111


audi = Audi()
print(audi.__dict__)

res = vars(audi)
print(res)
