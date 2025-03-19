# functions within functions aka leads into recursion
def mult(x):
    y = x * 2
    print(y)


def squared(x, y):
    return x(y)


print(squared(mult, 5))
