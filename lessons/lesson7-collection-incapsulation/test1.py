# Collections

# UserDict, UserList, UserDict added access to self.data
class MyList(list):
    def some(self):
        s = 0
        for i in self:
            s += i
        return s



a = MyList([1,2,23])

print(a.some())