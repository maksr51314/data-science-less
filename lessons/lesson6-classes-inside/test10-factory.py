# abstract factory
class Car:
    def __init__(self, *args):
        print('car')

class Boat:
    def __init__(self, *args):
        print('boat')

class Factory:
    def __new__(cls, *args, **kwargs):
        if args[0] == 'car':
            return Car(args[1::])

        if args[0] == 'boat':
            return Boat(args[1::])

        else:
            raise TypeError('it"s not a factory')


fac = Factory('car')
fac = Factory('boat')
