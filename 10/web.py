"""
Guide to Web Scraping
"""
from os import remove
from requests import get
from bs4 import BeautifulSoup


def main():
    """
    main function
    """
    res = get("http://www.example.com")
    print(type(res))
    print(res.text)
    soup = BeautifulSoup(res.text, features="html.parser")
    print(soup.select("title"))
    title_tag = soup.select("title")
    print(title_tag[0])
    print(type(title_tag[0]))
    print(title_tag[0].getText())

    res = get("https://en.wikipedia.org/wiki/Room_641A")
    soup = BeautifulSoup(res.text, features="html.parser")
    print(soup.select(".mw-headline"))
    for item in soup.select(".mw-headline"):
        print(item.text)

    res = get("https://en.wikipedia.org/wiki/Cicada_3301")
    soup = BeautifulSoup(res.text, features="html.parser")
    image_info = soup.select(".thumbimage")
    print(image_info)
    cicada = image_info[0]
    print(type(cicada))
    print(cicada["src"])
    image_link = get(
        "http://upload.wikimedia.org/wikipedia/en/thumb/7/7e/"
        + "Cicada_3301_logo.jpg/220px-Cicada_3301_logo.jpg"
    )
    print(image_link.content)
    with open("my_new_file_name.jpg", "wb") as file:
        file.write(image_link.content)

    base_url = "http://books.toscrape.com/catalogue/page-{}.html"
    res = get(base_url.format("1"))
    soup = BeautifulSoup(res.text, features="html.parser")
    print(soup.select(".product_pod"))
    products = soup.select(".product_pod")
    example = products[0]
    print(type(example))
    print(example.attrs)
    print(list(example.children))
    print(example.select(".star-rating.Three"))
    print(example.select(".star-rating.Two"))
    print(example.select("a"))
    print(example.select("a")[1])
    print(example.select("a")[1]["title"])

    two_star_titles = []
    for num in range(1, 51):
        print(base_url.format(num))
        res = get(base_url.format(num))
        soup = BeautifulSoup(res.text, features="html.parser")
        books = soup.select(".product_pod")
        for book in books:
            if len(book.select(".star-rating.Two")) != 0:
                two_star_titles.append(book.select("a")[1]["title"])
    print(two_star_titles)
    remove("my_new_file_name.jpg")


if __name__ == "__main__":
    main()
