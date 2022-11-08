def sum_of_two_numbers(first_number: int, second_number: int) -> int:
    result = first_number + second_number
    if 15 <= result <= 20:
        return 20
    else:
        return result


if __name__ == '__main__':
    print(sum_of_two_numbers(10, 5))
