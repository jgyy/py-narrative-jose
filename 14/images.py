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
    mac = image_open("example.jpg")
    mac.show()
    print(mac.size)
    print(mac.filename)
    print(mac.format_description)
    mac.crop((0, 0, 100, 100)).show()
    pencils = image_open("pencils.jpg")
    pencils.show()
    print(pencils.size)
    xint = 0
    yint = 0
    wint = 1950 // 3
    hint = 1300 // 10
    pencils.crop((xint, yint, wint, hint)).show()
    xint = 0
    yint = 1100
    wint = 1950 // 3
    hint = 1300
    pencils.crop((xint, yint, wint, hint)).show()
    print(mac.size)
    halfway = 1993 // 2
    xint = halfway - 200
    yint = 800
    wint = halfway + 200
    hint = 1257
    mac.crop((xint, yint, wint, hint)).show()
    computer = mac.crop((xint, yint, wint, hint))
    mac.paste(im=computer, box=(0, 0))
    mac.show()
    mac.paste(im=computer, box=(796, 0))
    print(mac)
    print(mac.size)
    hint, wint = mac.size
    new_h = int(hint / 3)
    new_w = int(wint / 3)
    mac.resize((new_h, new_w)).show()
    mac.resize((3000, 500)).show()
    pencils.rotate(90).show()
    pencils.rotate(90, expand=True).show()
    pencils.rotate(120).show()
    red = image_open("red_color.jpg")
    blue = image_open("blue_color.png")
    red.putalpha(128)
    red.show()
    blue.putalpha(128)
    blue.show()
    blue.paste(red, (0, 0), mask=red)
    blue.show()


if __name__ == "__main__":
    main()
