"""
Working with Simple Text Files
"""
from os.path import join, dirname


def main():
    """
    main function
    """
    test_file = join(dirname(__file__), "test_file.txt")
    with open(test_file, encoding="utf-8") as myfile:
        print(myfile.read())
        print(myfile.read())
        print(myfile.seek(0))
        print(myfile.read())
        myfile.seek(0)
        print(myfile.readlines())
        lines = myfile.read()
        print(lines)


if __name__ == "__main__":
    main()
