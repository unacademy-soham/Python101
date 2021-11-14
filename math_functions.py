NUMBER = 20

def add(a, b):
    return a+b


def multiply(a, b):
    return a*b


def power(a, b):
    res = 1
    for i in range(b):
        res *= a
    return res
