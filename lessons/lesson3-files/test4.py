import hashlib
import pickle

obj = {'a': [1, 2, 3], True: {'b': 123}}

# res = pickle.dumps(obj)
# # res = repr(obj)  # string
# obj1 = pickle.loads(res)
# print(res)
# print(obj1 == obj)  # by value
# print(obj1 is obj)  # by link


h = hashlib.sha256()
with open('obj.pickle', 'wb') as f:
    h.update(pickle.dump(obj, f))

# h.update(b'qqq111')
# print(h.digest())


with open('obj.pickle', 'rb') as f:
    pickle.load(f)

