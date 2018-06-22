# google proto buffer and YAML

import tempfile
import json

obj = {'a': [1, 2, 3], True: {'b': 123}}

res = json.dumps(obj)

res1 = json.loads(res)

print(res, res1)




f = tempfile.TemporaryFile()

f.write(b'aaaaa')

f.seek(0)
f.read()

print(f.name)

f.close()
