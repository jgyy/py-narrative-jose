"""
Functions
"""


def main():
    """
    main function
    """

    def lowercase_function_name(argument1, argument2, argument3="default value"):
        """
        This is the DocString of the function. It is where you can write a helpful
        description for anyone who will use your function.
        """
        print(argument1, argument2, argument3)

    lowercase_function_name("argument1", "argument2")

    def report_agent():
        print("Reporting Agent")

    report_agent()

    def report(name):
        print(f"Reporting {name}")

    report("Bond")

    def add(n_1, n_2):
        return n_1 + n_2

    result = add(2, 3)
    print(result)

    def secret_check(mystring):
        return "secret" in mystring

    print(secret_check("This is a secret."))
    print(secret_check("SECRET"))

    def code_maker(mystring):
        output = list(mystring)
        for i, letter in enumerate(mystring):
            for vowel in ["a", "e", "i", "o", "u"]:
                if letter.lower() == vowel:
                    output[i] = "x"
        output = "".join(output)
        return output

    print("".join(["a", "b", "c"]))
    print("--".join(["a", "b", "c"]))
    print("-x-".join(["a", "b", "c"]))
    print(code_maker("Edward"))
    print(code_maker("John"))


if __name__ == "__main__":
    main()
