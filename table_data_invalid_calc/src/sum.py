from functools import reduce


def sum(numbers):
    return reduce(lambda x, y: x+y*2, numbers)
