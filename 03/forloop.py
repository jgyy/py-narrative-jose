"""
for loop
"""


def main():
    """
    main function
    """
    mylist = [1, 2, 3, 4]
    for num in mylist:
        print(num)
    for totally_made_up in mylist:
        print(totally_made_up)
    for num in mylist:
        print(num, end=" ")
    for num in mylist:
        print("some unrelated variable, but print for every num in mylist")
    for letter in "This is a string recruit":
        print(letter)
    mystring = "This is a string recruit"
    for word in mystring.split():
        print(word)
    tup = (1, 2, 3, 4)
    for num in tup:
        print(num)
    list_of_tups = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
    for (num1, num2) in list_of_tups:
        print(num1)
        print(num2)
        print("\n")
    my_dictionary = {"a": 1, "b": 2, "c": 3}
    for item in my_dictionary:
        print(item)
    for k in my_dictionary.items():
        print(k)
        print("\n")
    for letter in "code":
        if letter == "d":
            continue
        print(f"Current Letter is: {letter}")


if __name__ == "__main__":
    main()
