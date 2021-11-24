"""
Python Strings
"""


def main():
    """
    main function
    """
    print("hello")
    print(" I'm not a spy! ")
    print("one")
    print("two")
    print("Special Codes")
    print("this is a new line \n notice how this prints")
    print("this is a tab \t notice how this prints")
    print("Notice how they both follow the general escape character of backslash ")
    word = "hello"
    print(word[0])
    print(word[3])
    print(word[-1])
    alpha = "abcdef"
    print(alpha[0:3])
    print(alpha[0:4])
    print(alpha[2:4])
    print(alpha[2:])
    print(alpha[:2])
    print(alpha[0:6:2])
    basic = "Hello world I am still a recruit"
    print(basic.upper())
    print(basic.lower())
    print(basic.split())
    print(basic.split("I"))
    user_name = "Recruit"
    print(f"Welcome {user_name}")
    action = "run"
    print(f"The {user_name} needs to {action}")
    num = 123.6789
    print(f"The code is: {num}")
    print(f"The code is: {num:.1f}")
    print(f"The code is: {num:.2f}")
    print(f"The code is: {num:.3f}")
    print(f"The code is: {num:.4f}")


if __name__ == "__main__":
    main()
