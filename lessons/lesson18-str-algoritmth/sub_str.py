s = 'the needle in the haystack'
p = 'needle'

# for index in range(len(s) - len(p) + 1):
#     if s[index:index + len(p)] == p:
#         print(index)
#         break

K = 127
def to_number(str):
    n = ord(str[0])
    for symbol in str:
        n = n * K + ord(symbol)
    return n

pn = to_number(p)
sn = to_number(s)

# def shift(sn, start, end):
#     sn -

for index in range(len(s) - len(p)):
    if (pn == sn):
        print(index)
        break;
    sn = shift(sn, s[index], s[index + len(p)])



print(sn)