import datetime

a1 = datetime.datetime.now()

a2 = datetime.datetime.now()

a1 = a1 + datetime.timedelta(hours=5)

a1 = a1.weekday()

print(a1)

# print(a.__format__('mm:ss'))