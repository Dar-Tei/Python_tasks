def sum_of_elements(l):  # Sum all the elements of a list
    the_whole_amount = 0
    for x in l:
        the_whole_amount += x

    return the_whole_amount


if __name__ == '__main__':
    print(sum_of_elements([1, 5, 9, 7, 9, 5]))
