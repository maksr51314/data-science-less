import csv

m = [('aaaa, "bbb', 123), ('qqqqqq', 234)]

s = open('m.csv', 'wt')
w = csv.writer(s)

for row in m:
    w.writerow(row)

s.close()


s1 = open('m.csv', 'rt')
r = csv.reader(s1)

for row in r:
    print(row)

# help(csv)
