import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 100)

print(x)

y1 = np.sin(2 * x)

y2 = np.sin(7 * x)

y3 = np.sin(11 * x)

y4 = np.sin(14 * x)

# plt.plot(y1)
# plt.show()
# plt.plot(y2)

y = y1 + y2 + y3 + y4

# plt.plot(y)

A = np.abs(np.fft.fft(y))**2

fr = np.fft.fftfreq(y.size)
idx = np.argsort(fr)

plt.plot(idx, A)

gr = np.gradient(A)
plt.plot(gr)
# plt.plot(A)
plt.show()


