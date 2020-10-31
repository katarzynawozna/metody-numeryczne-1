import math

def integral(n):
    if n == 1:
        return 1
    else:
        return math.e - (n + 1)*integral(n-1)

for n in range(1, 20):
    print(integral(n))