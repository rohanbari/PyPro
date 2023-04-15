import matplotlib.pyplot as plot
import numpy as np

# The number of dots being displayed
N = 1000

# Random x-y coordinates in [0, 1]
x = np.random.rand(N)
y = np.random.rand(N)

# Expansion of dots in [20, 120]
window_size = (5, 5)
size = 100*np.random.rand(N) + 20

# Random colors
colors = np.random.rand(N, 4)

plot.figure(figsize=window_size)
plot.scatter(x, y, c=colors, s=size)
plot.axis('off')
plot.show()
