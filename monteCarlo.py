import random
import math


def randomBr(min, max):
    return (max - min) * random.random() + min


def area(x, y):
    return x * y


def monteCarlo(fx, gx, xs, ys, trys=100000):
    hits = 0
    for i in range(trys):
        x = randomBr(xs[0], xs[1])
        y = randomBr(ys[0], ys[1])
        if gx(x) > y > fx(x):
            hits += 1
    if hits == 0:
        return 0
    return area(math.fabs(xs[1]-xs[0]), math.fabs(ys[1]-ys[0])) / (trys / hits)
