def key_verification(dictionary, user_key):
    return user_key in dictionary


if __name__ == '__main__':
    print(key_verification({"name": 'Yasha', "age": 19, "gender": "female"}, "home"))
