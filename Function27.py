
def type_checking(first, second):
    result = first + second
    if type(first) != int or type(second) != int:
        raise Exception("Summand types are incorrect")
    return result


if __name__ == '__main__':
    print(type_checking(10.15, 5))

