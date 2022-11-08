def multiplication_of_elements(l):  # Multiplies all elements of a list
    how_much_came_out = 1
    for x in l:
        how_much_came_out *= x

    return how_much_came_out


if __name__ == '__main__':
    print(multiplication_of_elements([1, 5, 9, 7, 9, 5]))
