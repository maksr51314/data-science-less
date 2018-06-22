import numpy as np
import matplotlib.pyplot as plt

def plotsub(x, y):
    plt.plot(x, y)

x = np.arange(0,10,1);
y = x*x

plotsub(x,y)
plotsub(x*10,y)
plt.show()