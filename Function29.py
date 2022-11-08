from math import sqrt


def euclidean_distance(x1, x2, y1, y2):
    d = sqrt(((x2 - x1)**2)+((y2 - y1)**2))
    return d


if __name__ == '__main__':
    print(euclidean_distance(10, 5, 3, 5))
