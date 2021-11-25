"""
List Comprehensions
"""
from numpy.random import shuffle, randint


def main():
    """
    main function
    """
    mylist = []
    for let in "word":
        mylist.append(let)
    print(mylist)
    myletters = list("word")
    print(myletters)
    squares = [x ** 2 for x in range(0, 11)]
    print(squares)
    evens = [x for x in range(0, 10) if x % 2 == 0]
    print(evens)
    mylist = [x if x % 2 == 0 else "not even" for x in range(0, 10)]
    print(mylist)


if __name__ == "__main__":
    main()
