from scipy import optimize

def f(x):
    return (2 * (x**4) + 24 * (x**3) + 61 * (x**2) - 16 * x + 1)

root = optimize.ridder(f, -10, -5)
# -8.123105625616667

root2 = optimize.ridder(f, -5, 1)
# -4.121320343558647

root3 = optimize.ridder(f, 0, 0.1214)
# 0.12132034355964337

root4 = optimize.ridder(f, 0.1214, 0)
# 0.12132034355964337