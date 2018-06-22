def a():
    print('a')


def b():
    print('b')


def c():
    print('c')


class Observerable:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def __call__(self, f):
        def wrapper(*args, **kwargs):
            res = f(*args, **kwargs)
            for observer in self._observers:
                observer()
            return res

        return wrapper


observer = Observerable()


@observer
def event():
    print('Event')



observer.attach(a)
observer.attach(b)

event()
