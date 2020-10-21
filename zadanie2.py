import matplotlib.pyplot as plt
import numpy as np


series = [0.1]

for current_number in list(range(1,100)):
    previous_number = current_number-1
    number = 3.5 * (series[previous_number]) * (1-(series[previous_number]))
    series.append(number)

n = np.linspace(1, 100, 100)

plt.scatter(series, n)
plt.show()