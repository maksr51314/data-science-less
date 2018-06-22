class IHidden(object):
    def m1(self):
        print('A.m1')

    def m2(self):
        print('A.m2')


class IProxy:
    def __init__(self):
        self._ihidden = IHidden()

    def m1(self):
        print('Proxy.m1')

    def __getattribute__(self, item):
        return getattr(self._ihidden, item)


proxy = IProxy()

proxy.m1()
# proxy.m2()
