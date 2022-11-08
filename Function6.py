def addition_of_rows(original_row):
    l = original_row.split(' ')

    try:
        l2 = l[1]
    except IndexError as e:
        print(f'The minimum number of words must be 2: {e}')
        return

    l1 = l[0]
    l2 = l[1]
    start1 = l1[0]
    end1 = l1[-1]
    start2 = l2[0]
    end2 = l2[-1]
    swapped_string = end1 + l1[1:-1] + start1 + " " + end2 + l2[1:-1] + start2
    return swapped_string


if __name__ == '__main__':
    print(addition_of_rows(input('Enter two words: ')))
