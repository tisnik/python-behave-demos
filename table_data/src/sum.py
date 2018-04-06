from functools import reduce


def sum(numbers):
    return reduce(lambda x, y: x+y, numbers)
