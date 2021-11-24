"""
Tuples
"""


def main():
    """
    main function
    """
    tup = (1, 2, 3)
    print(type(tup))
    tup = ("a", 1)
    print(tup[0])
    mylist = [1,2,3]
    print(type(mylist))
    mylist[0] = 'new'
    print(mylist)
    tup = ('a','b','c','a')
    print(tup.index('b'))
    print(tup.count('a'))


if __name__ == "__main__":
    main()
