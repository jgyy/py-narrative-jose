"""
Field Readiness
"""
from os.path import join, dirname


def main():
    """
    main function
    """
    exam = join(dirname(__file__), "exam.txt")
    with open(exam, encoding="utf-8") as file:
        exam_lines = file.readlines()
        print(exam_lines)
        len(exam_lines)
        print(exam_lines[4])
        last = exam_lines[-1]
        print(last)
        print(last[5])
        print(len(last))
        print(last.split())
        print(len(last.split()))
    dic = {"levelone": [1, 2, {"leveltwo": [5, 6, [1, ["get me please"]]]}]}
    print(dic["levelone"])
    print(dic["levelone"][2])
    print(dic["levelone"][2]["leveltwo"])
    print(dic["levelone"][2]["leveltwo"][2])
    print(dic["levelone"][2]["leveltwo"][2][1])
    print(dic["levelone"][2]["leveltwo"][2][1][0])
    mylist = [
        1,
        2,
        3,
        4,
        5,
        6,
        4,
        3,
        2,
        1,
        2,
        3,
        4,
        5,
        6,
        6,
        7,
        8,
        5,
        6,
        7,
        8,
        9,
        8,
        9,
        8,
        9,
        7,
        10,
        123,
        1,
        2,
        2,
        3,
        1,
        3,
        2,
        4,
        1,
        4,
        4,
        1,
        2,
        2,
        22,
        3,
        4,
        1,
        4,
        1,
    ]
    print(set(mylist))
    print(len(list(set(mylist))))


if __name__ == "__main__":
    main()
