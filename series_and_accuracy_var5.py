import math


def series_sum(n):
    sum_of_series = 0
    for i in range(1, n + 1):
        sum_of_series += (math.sqrt(i)) / (((4 * i ** 2) - 1) ** 2)
    return sum_of_series


if __name__ == '__main__':
    result = int(series_sum(100) * 10000) / 10000
    print(result)
