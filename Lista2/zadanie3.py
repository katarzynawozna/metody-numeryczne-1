def first_method(x):
    return (((x ** 2) + 1) ** (1 / 2)) - 1

def second_method(x):
    return (x ** 2) / ((((x ** 2) + 1) ** (1 / 2)) + 1)

for x in range(25):
    print(f"For {x} first method gives: {first_method(2 ** x)} \n second method gives {second_method(2 ** x)}")