# Heart-shaped graph using mathematics

import numpy as np
import matplotlib.pyplot as mp

t = np.linspace(0, 2*np.pi, 100)

x = 16*np.sin(t)**3
y = 13*np.cos(t) - 5*np.cos(2*t) - 2*np.cos(3*t) - np.cos(4*t)

mp.plot(x, y, c=(1, 0.2, 0.5), lw=20)

mp.title('To mathematics:')
mp.axis('equal')
mp.axis('off')

mp.show()
