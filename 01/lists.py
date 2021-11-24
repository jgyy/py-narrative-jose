"""
Python Lists
"""


def main():
    """
    main function
    """
    my_list = [1, 2, 3]
    print(my_list)
    my_list2 = ["a", "b", "c"]
    print(my_list2)
    aint = 100
    bint = 200
    cint = 300
    my_list3 = [aint, bint, cint]
    print(my_list3)
    mylist = ["a", "b", "c", "d"]
    print(mylist[0])
    print(mylist[0:3])
    print(len("string"))
    print(len(my_list))
    mylist = [1, 2, 3]
    mylist.append(4)
    print(mylist)
    mylist.pop()
    print(mylist)
    mylist.append(4)
    print(mylist)
    item = mylist.pop()
    print(item)
    print(mylist)
    first_item = mylist.pop(0)
    print(first_item)
    print(mylist)
    mylist = [1, 2, 3]
    mylist.reverse()
    print(mylist)
    mylist.sort()
    print(mylist)
    result = mylist.reverse()
    print(result)
    mylist = [1, 2, 3]
    mylist.insert(0, "NEW")
    print(mylist)
    new_list = [1,2,3,['a','b','c']]
    print(type(new_list))
    print(new_list[3])
    print(new_list[3][0])


if __name__ == "__main__":
    main()
