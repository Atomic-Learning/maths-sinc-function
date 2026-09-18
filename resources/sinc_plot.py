import scipy.special
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 1000)
y = scipy.special.sinc(x)

plt.plot(x, y)
plt.title("Sinc Function")
plt.xlabel("x")
plt.ylabel("sinc(x)")
plt.grid(True)
plt.savefig("resources/sinc_plot.png")