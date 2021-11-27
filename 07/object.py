"""
Object Oriented Programming
"""


class Sample:
    """
    sample class
    """

    def __init__(self):
        pass

    def __call__(self):
        pass

    def __delattr__(self, __name):
        pass


class Circle:
    """
    circle class
    """

    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        """
        area method
        """
        return self.radius * self.radius * Circle.pi

    def perimeter(self):
        """
        perimeter method
        """
        return 2 * self.radius * Circle.pi


class Person:
    """
    person class
    """

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def report(self):
        """
        report method
        """
        print(f"I am {self.first_name} {self.last_name}.")

    @staticmethod
    def hello():
        """
        hello static method
        """
        print("Hello!")


class Agent(Person):
    """
    agent class
    """

    planet = "Earth"

    def __init__(self, first_name, last_name, code_name):
        Person.__init__(self, first_name, last_name)
        self.code_name = code_name

    def report(self):
        """
        report method
        """
        print("Sorry I can not give you my real name")
        print(f"You can call me {self.code_name}")

    def true_name(self, passcode):
        """
        true name method
        """
        if passcode == 123:
            print("Thank you for providing the passcode")
            print(f"I am {self.first_name} {self.last_name}.")
        else:
            self.report()

    @staticmethod
    def _private_methods():
        print("Privacy Please.")


class Book:
    """
    book class
    """

    def __init__(self, title, author, pages):
        print("A book is created")
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"Title: {self.title} , author:{self.author}, pages: {self.pages}."

    def __len__(self):
        return self.pages

    def __del__(self):
        print("A book is destroyed")


def main():
    """
    main function
    """
    mylist = [1, 2, 3]
    print(mylist.count(2))
    print(type(1))
    print(type([]))
    print(type(()))
    print(type({}))
    xsample = Sample()
    print(type(xsample))
    magent = Agent(first_name="Alan", last_name="Turing", code_name="Hero")
    print(magent.planet)
    magent.hello()
    magent.true_name(100)
    magent.true_name(123)
    cir = Circle(radius=2)
    print(f"Radius is: {cir.radius}")
    print(f"Area is: {cir.area()}")
    cir.radius = 10
    print(cir.area())
    book = Book("Python Rocks!", "Jose Portilla", 159)
    print(book)
    print(len(book))
    del book


if __name__ == "__main__":
    main()
