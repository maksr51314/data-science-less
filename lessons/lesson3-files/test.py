# with open("ad_lesbiam.txt") as fobj:
#     for line in fobj:
#         print(line.rstrip())
#
# fh = open("example.txt", "w")
# fh.write("To write or not to write\nthat is the question!\n")
# fh.close()


# with open("example.txt") as fobj:
#     for line in fobj:
#         print(line.rstrip())

f = open('file.txt', 'w')  # write
f = open('file.txt', 'a')  # append
f = open('file.txt', 'x')  # create but don't touch exist
f = open('file.txt', 'r')  # read
f = open('file.txt', 'wt')  # text uft-8
f = open('file.txt', 'wb')  # binary

# f.flush()  # wrire  immediatelly
# f.tell # указатель
