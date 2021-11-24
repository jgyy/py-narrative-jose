"""
Python Numbers
"""


def main():
    """
    main function
    """
    print(100)
    print(type(100))
    print(1.2)
    print(type(1.2))
    print(type(100.0))
    print(type(100.0))
    print(1 + 1)
    print(2 - 1)
    print(2 * 2)
    print(3 / 2)
    print(1 / 1)
    print(2 ** 3)
    print(2 ** (1 / 2))
    print(1 + 2 * 1000 + 1)
    print((1 + 2) * (1000 + 1))
    avar = 2
    print(type(avar))
    print(avar + 3)
    bvar = 3
    print(avar + bvar)
    avar = 1000
    print(avar + bvar)
    print(avar)
    avar += avar
    print(avar)
    message = 111
    hash_code = 346728236
    secret_message = message * hash_code
    print(secret_message)
    decrypted_message = secret_message / hash_code
    print(decrypted_message)


if __name__ == "__main__":
    main()
