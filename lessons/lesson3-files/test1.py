# f = open('example.txt', 'rt')
# s = f.read()
# print(s)
#
#
# # by string
# f1 = open('example.txt', 'rt')
# s1 = f1.readline()
# print(s1)
#
# # by symbol
# f1 = open('example.txt', 'rt')
# s1 = f1.read(4)
# print(s1)
#
# f.close()
# f1.close()

f = open('example.txt', 'wt')
# for line in f:
#     print(line)

f.close()

f = open('example.txt', 'rt')
for line in f:
    print(line)

f.close()
