"""
Dictionaries
"""


def main():
    """
    main function
    """
    dic = {"key1": "value1", "key2": "value2"}
    print(dic["key1"])
    print(dic["key2"])
    dic["new_key"] = "new item"
    print(dic)
    dic = {"a": 1, "z": 2}
    print(dic)
    dic["new"] = 0
    print(dic)
    dic["za"] = "hello"
    print(dic)
    dic = {
        "k1": 10,
        "k2": "stringy",
        "k3": [
            1,
            2,
            3,
        ],
        "k4": {"inside_key": 100},
    }
    print(dic)
    print(dic["k1"])
    print(dic["k2"])
    print(dic["k3"])
    print(dic["k3"][0])
    print(dic["k4"])
    print(dic["k4"]["inside_key"])
    code_names = {
        "Obama": "Renegade",
        "Bush": "Trailblazer",
        "Reagan": "Rawhide",
        "Ford": "Passkey",
    }
    print(code_names["Ford"])
    pop_in_mil = {"USA": 323, "Germany": 83, "India": 1324}
    print(pop_in_mil["USA"])
    print(code_names.keys())
    print(code_names.values())
    print(code_names.items())


if __name__ == "__main__":
    main()
