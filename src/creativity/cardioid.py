# A beautiful cardioid-shaped graph plot

import matplotlib.pyplot as mpl
import numpy as np

t = np.linspace(0, 2*np.pi, 100)
r = 1 - np.cos(t)

mpl.polar(t, r, lw=1.0)
mpl.axis('off')
mpl.show()
