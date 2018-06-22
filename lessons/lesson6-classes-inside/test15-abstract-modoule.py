from abc import abstractmethod, ABCMeta


class AbsValue(metaclass=ABCMeta):
    @abstractmethod
    def __set__(self, instance, value):
        pass

    @abstractmethod
    def __get__(self, instance, owner):
        pass


class Value(AbsValue):
    def __init__(self, v):
        self.v = v

    def __set__(self, instance, value):
        self.v = instance

    def __get__(self, instance, owner):
        return self.v


class Value1(AbsValue):
    def __get__(self, instance, owner):
        pass

    def __set__(self, instance, value):
        pass
