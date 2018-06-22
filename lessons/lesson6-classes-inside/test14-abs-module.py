import abc  # abstract base classes


# can't create object
class A(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def f(self):
        pass


# need to realise class A
class B:
    def f(self):
        pass


a = B()
