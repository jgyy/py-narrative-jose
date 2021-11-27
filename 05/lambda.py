"""
Lambda Expressions, Map, and Filter
"""


def main():
    """
    main function
    """
    square = lambda num: num ** 2
    my_nums = [1, 2, 3, 4, 5]
    print(list(map(square, my_nums)))

    def splicer(mystring):
        if len(mystring) % 2 == 0:
            return "even"
        return mystring[0]

    mynames = ["John", "Cindy", "Sarah", "Kelly", "Mike"]
    print(list(map(splicer, mynames)))

    def check_even(num):
        return num % 2 == 0

    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(list(filter(check_even, nums)))
    print(square(2))
    print(list(map(lambda num: num ** 2, my_nums)))
    print(list(filter(lambda n: n % 2 == 0, nums)))


if __name__ == "__main__":
    main()
