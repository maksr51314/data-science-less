import numpy as np

s1 = 'HEAD'
s2 = 'HEART'

if len(s2) < len(s1):
    s1, s2 = s2, s1

source = np.array(tuple(s1))
target = np.array(tuple(s2))

prev_row = np.arange(len(s1) + 1)

for el in target:
    current_row = (prev_row[1:], (source != el) + prev_row[1:])
    print(current_row)


print(source, target, prev_row)
