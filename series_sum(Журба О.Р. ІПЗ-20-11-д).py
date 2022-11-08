import math


def series_sum(accuracy: float) -> float:
    n = 1
    x = (math.sqrt(n)) / (((4 * n ** 2) - 1) ** 2)
    s = 0
    while abs(x) > accuracy:
        s += x
        n += 1
    return s


if __name__ == '__main__':
    print(series_sum(0.0001))
