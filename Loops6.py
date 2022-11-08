if __name__ == '__main__':
    n = int(input('enter the number: '))
    fact = 1
    for i in range(2, n+1):
        fact *= i
    print('Your factorial: ', fact)
