"""
Overview of Working with Images
"""
from os.path import join, dirname
from PIL import Image

image_open = lambda x: Image.open(join(dirname(__file__), x))


def main():
    """
    main function
    """
    links = image_open("Blue_Mission_Files/image_link.PNG")
    print(links.size)
    links.show()
    cover = image_open("Blue_Mission_Files/cover_image.PNG")
    print(cover.size)
    cover.show()
    cover = cover.resize(links.size)
    print(cover.size)
    cover.putalpha(200)
    cover.show()
    links.paste(cover,(0,0),cover)
    links.show()


if __name__ == "__main__":
    main()
