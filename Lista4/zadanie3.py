import numpy as np
import math

def satrun_speed(u, M0, m, g, v, t):
    for t in np.arange(0.0, 100, 0.001):
        velocity = u * math.log(M0 / (M0 - m * t)) - (g * t)
        if velocity >= 335: break
    return t

u = 2510
M0 = 2.8 * 10 ** 6
m = 13.3 * 10 ** 3
g = 9.81
v, t = 0

print(f"Velocity of Satrun V will reach 335 m/s after {satrun_speed(u, M0, m, g, v, t)} seconds")
