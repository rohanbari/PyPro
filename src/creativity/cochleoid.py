# The famous Cochleoid shape

import numpy as np
import matplotlib.pyplot as mpl

t = np.linspace(-20, 20, 10000)

x = np.sin(t)*np.cos(t) / t
y = np.sin(t)**2 / t

mpl.plot(x, y, lw=1.0)
mpl.axis('off')
mpl.show()
