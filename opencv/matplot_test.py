import numpy as np
import matplotlib
#matplotlib.use("TkAgg")
matplotlib.use("QT5Agg")

from matplotlib import pyplot as plt

x=np.arange(1,11)
y=2*x
plt.title("test")
plt.plot(x,y)
plt.show()

