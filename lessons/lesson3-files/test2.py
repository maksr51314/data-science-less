#
# # file lock parameters
# import fcntl
#
# f = open('example.txt', 'rt')
#
# fcntl.lockf(f, fcntl.LOCK_SH)
# fcntl.lockf(f, fcntl.LOCK_EX)
#
# fcntl.lockf(f, fcntl.LOCK_UN)
#
# f.close()

# dead lock //// live lock
f = open('example.txt', 'r+t')  # read and write for text
# help(f.seek)
f.seek(10)

res = f.tell()

print(res)
f.close()
