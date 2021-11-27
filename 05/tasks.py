"""
Functions Tasks
"""


def main():
    """
    main function
    """

    def check_ten(n_1, n_2):
        return (n_1 + n_2) == 10

    print(check_ten(10, 0))
    print(check_ten(5, 5))
    print(check_ten(2, 7))

    def check_ten_sum(n_1, n_2):
        if (n_1 + n_2) == 10:
            return True
        return n_1 + n_2

    print(check_ten_sum(10, 0))
    print(check_ten_sum(2, 7))

    def first_upper(mystring):
        return mystring[0].upper()

    print(first_upper("hello"))
    print(first_upper("agent"))

    def last_two(mystring):
        if len(mystring) < 2:
            return "Error"
        return mystring[-2:]

    print(last_two("hello"))
    print(last_two("hi"))
    print(last_two("a"))

    def seq_check(nums):
        for i in range(len(nums) - 2):
            if nums[i] == 1 and nums[i + 1] == 2 and nums[i + 2] == 3:
                return True
        return False

    print(seq_check([1, 2, 3]))
    print(seq_check([7, 7, 7, 1, 2, 3, 7, 7, 7]))
    print(seq_check([3, 2, 1, 3, 2, 1, 1, 1, 2, 2, 3, 3, 3]))

    def compare_len(s_1, s_2):
        return abs(len(s_1) - len(s_2))

    print(compare_len("aa", "aa"))
    print(compare_len("a", "bb"))
    print(compare_len("bb", "a"))

    def sum_or_max(mylist):
        length = len(mylist)
        if length % 2 == 0:
            return sum(mylist)
        return max(mylist)

    print(sum_or_max([1, 2, 3]))
    print(sum_or_max([0, 1, 2, 3]))

    def replace_and_switch(name):
        output = list(range(len(name)))
        for i, letter in enumerate(name):
            if letter.lower() in ["a", "e", "i", "o", "u"]:
                output[i] = "x"
            else:
                output[i] = letter
        last = output[-1]
        first = output[0]
        output[0] = last
        output[-1] = first
        return "".join(output)

    print(replace_and_switch("James"))
    print(replace_and_switch("Cindy"))
    print(replace_and_switch("Alfred"))


if __name__ == "__main__":
    main()
