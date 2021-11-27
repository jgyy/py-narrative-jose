"""
Unzipping and Zipping Files
"""
from os import walk
from os.path import join, dirname
from shutil import unpack_archive
from re import findall, search


def main():
    """
    main function
    """
    unpack_archive(
        join(
            dirname(__file__), "Mission_Orange_Files", "unzip_me_for_instructions.zip"
        ),
        join(dirname(__file__), "Mission_Orange_Files", "extracted_content"),
        "zip",
    )
    pattern = r"https://[-?_=./\w]+"
    test = (
        "here is a website https://drive.google.com/open?id=1tWJBFrSQL06qTZgkohs4t_a5Cu84AheLo"
        + " and https://docs.google.com/document/d/Q-DcxM17nJm_El0aGsNnY7FajaogRviwja/edit"
        + " let's see if we can find it."
    )
    print(findall(pattern, test))

    def search_func(file, pattern=r"https://[-?_=./\w]+"):
        with open(file, "r", encoding="utf-8") as fil:
            text = fil.read()
        if search(pattern, text):
            return search(pattern, text)
        return ""

    results = []
    for folder, _, files in walk(
        join(dirname(__file__), "Mission_Orange_Files", "extracted_content")
    ):
        for fil in files:
            full_path = join(folder, fil)
            results.append(search_func(full_path))
    for res in results:
        if res != "":
            print(res.group())


if __name__ == "__main__":
    main()
