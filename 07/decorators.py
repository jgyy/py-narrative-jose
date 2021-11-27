"""
Decorators
"""


def main():
    """
    main function
    """

    def my_func():
        print("hello")

    my_func()

    def func():
        return 1

    print(func())
    print(locals())
    print(globals())
    print(globals().keys())
    print(globals()["__name__"])

    def hello(name="Jose"):
        print("The hello() function has been executed")
        print(name)

        def greet():
            return "\t This is inside the greet() function"

        def welcome():
            return "\t This is inside the welcome() function"

        print(greet())
        print(welcome())
        print("Now we are back inside the hello() function")

    hello()
    greet = hello
    print(greet())

    def other(func):
        print('Other code would go here')
        print(func())

    other(hello)

    def new_decorator(func):

        def wrap_func():
            print("Code would be here, before executing the func")

            func()

            print("Code here will execute after the func()")

        return wrap_func

    @new_decorator
    def func_needs_decorator():
        print("This function is in need of a Decorator")

    func_needs_decorator()


if __name__ == "__main__":
    main()
