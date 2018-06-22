import numpy as np
import numpy.random as rnd
import matplotlib.pyplot as plt

a = rnd.rand(3, 4)
b = rnd.rand(3, 4)
print(a)
print(b)

print(a @ b.T)

# x = np.linspace(0, 2*np.pi, 50)
# y = np.sin(x)
#
# # plt.plot(x, y)
#
# dy = y[1:] - y[:-1]

# plt.plot(x[1:], dy)
# plt.show()

b = a[a>0.5]
print(a>0.5)

c = rnd.uniform(0, 10, 1000)
# c = c.astype('int')

hu = np.histogram(c, bins=40)


n = rnd.normal(0, 1, 1000000)
hi = np.histogram(n, bins=101)

plt.plot(hi[1][1:], hi[0])
plt.show()
