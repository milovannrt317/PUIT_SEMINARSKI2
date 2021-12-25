import math
import monteCarlo as mnt


def findVertex(a, b, func):
    x = -b / (2 * a)
    y = func(x)
    return x, y


# -1 za beskonacnu povrsinu, 0 za presek u jednoj tacki i kad nema preseka
def findIntersection(a1, b1, c1, a2, b2, c2, func1, func2, v1, v2):
    if (a1 - a2) == 0:
        return -1

    x = findRoots(a1 - a2, b1 - b2, c1 - c2)

    if type(x[0]) is complex:
        if a1 * a2 > 0:
            return -1
        else:
            return 0
    if x[0] == x[1]:
        return 0

    x = (min(x[0], x[1]), max(x[0], x[1]))
    y = (min(v1[1], v2[1]), max(v1[1], v2[1]))

    granicax1 = x[0] if x[0] > 0 else 0
    granicax2 = x[1] if x[1] > 0 else 0
    granicay1 = y[0] if y[0] > 0 else 0
    granicay2 = y[1] if y[1] > 0 else 0


    if v1[1] > v2[1]:
        return mnt.monteCarlo(func2, func1, (granicax1, granicax2), (granicay1,granicay2) )
    else:
        return mnt.monteCarlo(func1, func2, (granicax1, granicax2), (granicay1,granicay2) )


def findRoots(a, b, c):
    d = discriminant(a, b, c)
    if d < 0:
        return complex(-b / (2 * a), math.sqrt(math.fabs(d))), complex(-b / (2 * a), -math.sqrt(math.fabs(d)))
    else:
        return ((-b + math.sqrt(d)) / (2 * a)), ((-b - math.sqrt(d)) / (2 * a))


def discriminant(a, b, c):
    return b * b - 4 * a * c
