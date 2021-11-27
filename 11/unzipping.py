"""
Unzipping and Zipping Files
"""
from zipfile import ZipFile, ZIP_DEFLATED
from send2trash import send2trash


def main():
    """
    main function
    """
    with open("new_file.txt", "w+", encoding="utf-8") as file:
        file.write("Here is some text")
    with open("new_file2.txt", "w+", encoding="utf-8") as file:
        file.write("Here is some text")
    with ZipFile("comp_file.zip", "w") as comp_file:
        comp_file.write("new_file.txt", compress_type=ZIP_DEFLATED)
        comp_file.write('new_file2.txt',compress_type=ZIP_DEFLATED)
    with ZipFile("comp_file.zip", "r") as zip_obj:
        zip_obj.extractall("extracted_content")
    send2trash("new_file.txt")
    send2trash("new_file2.txt")
    send2trash("comp_file.zip")


if __name__ == "__main__":
    main()
