import numpy as np
import matplotlib.pyplot as plot

t = np.linspace(0, 100, 10000)

x = np.sin(t)*(np.exp(np.cos(t)) - 2*np.cos(4*t) - np.sin(t/12)**5)
y = np.cos(t)*(np.exp(np.cos(t)) - 2*np.cos(4*t) - np.sin(t/12)**5)

plot.title('The Butterfly Curve')
plot.plot(x, y, c=(1, 0.2, 0.5), lw=0.5)
plot.axis('off')
plot.show()
