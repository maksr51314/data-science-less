import re

a = re.findall(r'\d+', '2131232 13123213 1')
print(help(a))

import enum


class Direction(enum.Enum):
    up = False
    right = False
    left = True
    down = False


a = Direction.up == Direction.up

import collections

class myCol(collections)
