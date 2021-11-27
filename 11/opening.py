"""
Opening and Reading Files
"""
from os import getcwd, listdir, walk
from os.path import join
from shutil import move, Error
from send2trash import send2trash


def main():
    """
    main function
    """
    with open("practice.txt", "w+", encoding="utf-8") as file:
        file.write("test")
    print(getcwd())
    print(listdir())
    print(listdir("/"))
    try:
        move("practice.txt", join(getcwd(), "11"))
    except Error as err:
        print(err)
    print(listdir())
    send2trash(join(getcwd(), "11", "practice.txt"))
    print(listdir())
    print(getcwd())
    for folder, sub_folders, files in walk(getcwd()):
        print("Currently looking at folder: " + folder)
        print("\n")
        print("THE SUBFOLDERS ARE: ")
        for sub_fold in sub_folders:
            print("\t Subfolder: " + sub_fold)
        print("\n")
        print("THE FILES ARE: ")
        for file in files:
            print("\t File: " + file)
        print("\n")


if __name__ == "__main__":
    main()
