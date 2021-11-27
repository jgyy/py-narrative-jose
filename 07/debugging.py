"""
Debugging and Timing Code
"""
from datetime import time, date, datetime


def main():
    """
    main function
    """
    yint = 2
    zint = 3
    result = yint + zint
    print(result)
    tim = time(1, 15, 5)
    print(tim.hour)
    print(tim.minute)
    print(tim.second)
    print(tim.microsecond)
    print(date.today())
    print(datetime.now())
    ti0 = datetime.now()
    result = [x ** 2 for x in range(10000)]
    ti1 = datetime.now()
    diff = ti1 - ti0
    print(diff.microseconds)
    print(diff)


if __name__ == "__main__":
    main()
