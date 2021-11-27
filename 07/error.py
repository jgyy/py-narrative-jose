"""
Error Handling and Exceptions
"""
from os import remove


def main():
    """
    main function
    """
    try:
        with open("testfile", "w", encoding="utf-8") as file:
            file.write("Test write this")
    except IOError:
        print("Error: Could not find file or read data")
    else:
        print("Content written successfully")
    try:
        with open("testfile", "r", encoding="utf-8") as file:
            file.write("Test write this")
    except IOError:
        print("Error: Could not find file or read data")
    else:
        print("Content written successfully")
    try:
        with open("testfile", "w", encoding="utf-8") as file:
            file.write("Test write this")
    finally:
        print("Always execute finally code blocks")
    try:
        with open("testfile", "r", encoding="utf-8") as file:
            file.write("Test write this")
    except IOError:
        print("Error: Could not find file or read data")
    finally:
        print("I always print, even if there was an exception!")
    remove("testfile")


if __name__ == "__main__":
    main()
