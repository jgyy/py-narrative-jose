"""
Control Flow Basics
"""


def main():
    """
    main function
    """
    if 1 < 2:
        print("One is less than two")
    if 1 > 2:
        print("One is greater than two")
    else:
        print("First if was not True")
    agent_code = 231912
    access = False
    if agent_code == 12345:
        print('Code Reset')
        print("Please call a supervisor")
    elif agent_code == 231912:
        print('Welcome Agent')
        print('Setting Your Access to True')
        access = True
    else:
        print("Sorry Wrong Code Supplied")
    if access:
        print('Access Granted')
    else:
        print('Access Denied')


if __name__ == "__main__":
    main()
