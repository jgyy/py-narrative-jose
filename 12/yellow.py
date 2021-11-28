"""
Yellow Mission Debrief
"""
from os.path import join, dirname
from csv import reader
from re import search
from PyPDF2 import PdfFileReader

fil = lambda x: join(dirname(__file__), "Yellow-Mission-Files", x)


def main():
    """
    main function
    """
    with open(fil("download_link.csv"), "r", encoding="utf-8") as file:
        c_read = reader(file)
        website = ""
        for row in c_read:
            website += row[2]
        print(website)
    test = (
        "This is a test string to practice re. "
        + "Email is test@example.com but don't pick: @twitter gmail.com or hi@hi ."
    )
    matches = search(r"[\w_.-]+@[\w_.-]+", test)
    print(matches.group())

    with open(fil("Contact_Email_Information.pdf"), "rb") as file:
        pdf = PdfFileReader(file)
        print(pdf.numPages)
        print(pdf.getPage(0))
        for num in range(pdf.numPages):
            page = pdf.getPage(num)
            page_text = page.extractText()
            match = search(r"[\w.-]+@[\w.-]+", page_text)
            if match:
                print(match.group())
        for num in range(pdf.numPages):
            page = pdf.getPage(num)
            page_text = page.extractText()
            match = search(r"[\w.-]+@[\w.-]+(.com|.net|.org)", page_text)
            if match:
                print(match.group())


if __name__ == "__main__":
    main()
