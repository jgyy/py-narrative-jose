"""
Sets
"""


def main():
    """
    main function
    """
    xset = set()
    xset.add(1)
    print(xset)
    xset.add(2)
    print(xset)
    xset.add(1)
    print(xset)
    mylist = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3]
    print(set(mylist))
    myset = {1, 2, 3}
    print(type(myset))


if __name__ == "__main__":
    main()
