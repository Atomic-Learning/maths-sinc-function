import scipy.special
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 1000)
y = scipy.special.sinc(x)
y_pos_asymptote = 1 / (np.pi * x)
y_neg_asymptote = -1 / (np.pi * x)

# Break the asymptote curves near x=0 to avoid a vertical connection line.
near_zero = np.abs(x) < 0.2
y_pos_asymptote[near_zero] = np.nan
y_neg_asymptote[near_zero] = np.nan

plt.plot(x, y, label="sinc(x)")
plt.plot(x, y_pos_asymptote, label="1/(pi x)", linestyle=":", color="tab:orange", alpha=0.55)
plt.plot(x, y_neg_asymptote, label="-1/(pi x)", linestyle=":", color="tab:green", alpha=0.55)
plt.title("Sinc Function")
plt.xlabel("x")
plt.ylabel("sinc(x)")
plt.ylim(-0.25, 1.1)
plt.xlim(-10, 10)
plt.grid(True)
plt.legend()
plt.savefig("resources/sinc_plot.png")