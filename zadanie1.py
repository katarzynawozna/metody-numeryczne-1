import matplotlib.pyplot as plt
import math
import numpy as np

y = []
x = []
for z in np.linspace(0, 1.5, 100):
    y.append((math.cos(z)) - 3*(math.sin(math.tan(z)-1)))
    x.append(z)

plt.plot(x, y)
plt.grid(True)
plt.show()
