"""
Nested Statements and Scope
"""


def main():
    """
    main function
    """
    xstr = "outside"

    def report():
        xreport = "inside"
        return xreport

    print(report())
    print(xstr)

    def enclosing():
        xenclose = "Enclosing Level"

        def inside():
            print(xenclose)

        inside()

    enclosing()

    def myfunc(xmy):
        print(f"X is {xmy}")
        xmy = "redefined inside myfunc()"
        print(f"X is {xmy}")

    myfunc(xstr)
    print(xstr)


if __name__ == "__main__":
    main()
