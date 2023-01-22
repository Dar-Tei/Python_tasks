def pangram_check(sentence):
    """this function compares two sets for intersection,
    returns True in case of complete intersection,
    False in the opposite case"""
    return set('abcdefghijklmnopqrstuvwxyz') == set(sentence.lower().replace(' ', ''))


if __name__ == '__main__':
    print(pangram_check("The quick brown fox jumps over the lazy dog"))
    help(pangram_check)
