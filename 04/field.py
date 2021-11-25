"""
Field Readiness
"""
from numpy.random import randint


def main():
    """
    main function
    """
    mystring = "Secret agents are super good at staying hidden."
    for word in mystring.split():
        first_letter = word.lower()[0]
        if first_letter == "s":
            print(word)
    for word in mystring.split():
        if len(word) % 2 == 0:
            print(word)
    mystring = "Secret agents are super good at staying hidden."
    print([word[0] for word in mystring.split()])
    print([n for n in range(0, 11) if n % 2 == 0])
    print(list(range(0, 11, 2)))
    result = []
    for _ in range(0, 10):
        result.append(randint(0, 100))
    print(result)
    print([randint(0, 100) for n in range(0, 10)])
    result = 3
    while result % 2 != 0:
        num = int(input("Please provide an even number: "))
        if num % 2 != 0:
            result = 1
        else:
            print("Thank you")
            result = 2


if __name__ == "__main__":
    main()
