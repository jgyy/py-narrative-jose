"""
Control Flow Basics
"""


def main():
    """
    main function
    """
    xint = 0
    while xint < 3:
        print("X is currently")
        print(xint)
        print("Adding 1 to x")
        xint += 1
    saved_input = input("Please input a number: ")
    print(saved_input)
    print("Welcome Agent")
    passcode = 0
    while passcode != 123:
        passcode = int(input("Please provide your passcode: "))
        if passcode != 123:
            print("Sorry wrong passcode provided")
            print("Try Again")
            print('\n')
    print("Correct Passcode!")
    xint = 0
    while xint < 10:
        print(xint)
        print('add one to x')
        xint += 1
        if xint == 3:
            break


if __name__ == "__main__":
    main()
