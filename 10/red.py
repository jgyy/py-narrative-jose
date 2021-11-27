"""
RED Mission Debrief
"""
from requests import get
from bs4 import BeautifulSoup


def main():
    """
    main function
    """
    res = get("https://www.thegoldbugs.com/blog")
    soup = BeautifulSoup(res.text, features="html.parser")
    blog = soup.select(".sqs-block-content > pre ")
    print(blog)
    text = blog[0]
    text = text.contents[0]
    print(text)
    print(text.split("-----"))
    result = ""
    for sentence in text.split("-----")[1:]:
        result = result + sentence[0]
    print(result)


if __name__ == "__main__":
    main()
