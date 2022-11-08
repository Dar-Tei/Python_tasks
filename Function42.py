def recursive_factorial(n):
    if n == 1:
        return n
    else:
        return n * recursive_factorial(n - 1)


if __name__ == '__main__':
    print(recursive_factorial(10))
