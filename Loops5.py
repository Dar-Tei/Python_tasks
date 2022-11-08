if __name__ == '__main__':
    import random
    L = [random.randint(0, 15) for i in range(10)]
    L2 = []
    print(L)
    for i in range(10):
        I = (len(L)-1)-i
        L2.append(L[I])
    print(L2)
