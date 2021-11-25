"""
Useful Operators
"""
from numpy.random import shuffle, randint


def main():
    """
    main function
    """
    print(range(0, 11))
    print(list(range(0, 11)))
    print(list(range(0, 12)))
    print(list(range(0, 11, 2)))
    print(list(range(0, 101, 10)))
    index_count = 0
    for letter in "abcde":
        print(f"At index {index_count} the letter is {letter}")
        index_count += 1
    for i, letter in enumerate("abcde"):
        print(f"At index {i} the letter is {letter}")
    print(list(enumerate("abcde")))
    mylist1 = [1, 2, 3, 4, 5]
    mylist2 = ["a", "b", "c", "d", "e"]
    print(zip(mylist1, mylist2))
    print(list(zip(mylist1, mylist2)))
    for item1, item2 in zip(mylist1, mylist2):
        print(f"For this tuple, first item was {item1} and second item was {item2}")
    print("x" in ["x", "y", "z"])
    print("x" in [1, 2, 3])
    mylist = [10, 20, 30, 40, 100]
    print(min(mylist))
    print(max(mylist))
    shuffle(mylist)
    print(mylist)
    print(randint(0, 100))
    input("Enter Something into this box: ")
    print(1 < 2)
    print(1 > 2)
    print(1 <= 3)
    answer = "no"
    if answer != "yes":
        print("Success!")


if __name__ == "__main__":
    main()
