"""
Working with PDF Files
"""
from os.path import join, dirname
from PyPDF2 import PdfFileReader, PdfFileWriter


fil = lambda x: join(dirname(__file__), x)


def main():
    """
    main function
    """
    with open(fil("Working_Business_Proposal.pdf"), "rb") as file:
        pdf_reader = PdfFileReader(file)
        print(pdf_reader.numPages)
        page_one = pdf_reader.getPage(0)
        page_one_text = page_one.extractText()
        print(page_one_text)

    with open(fil("Working_Business_Proposal.pdf"), "rb") as file:
        pdf_reader = PdfFileReader(file)
        first_page = pdf_reader.getPage(0)
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(first_page)

    with open(fil("Some_New_Doc.pdf"), "wb") as pdf_output:
        pdf_writer.write(pdf_output)

    with open(fil("Working_Business_Proposal.pdf"), "rb") as file:
        pdf_reader = PdfFileReader(file)
        pdf_text = []
        for pag in range(pdf_reader.numPages):
            page = pdf_reader.getPage(pag)
            pdf_text.append(page.extractText())
        print(pdf_text)
        print(pdf_text[3])


if __name__ == "__main__":
    main()
