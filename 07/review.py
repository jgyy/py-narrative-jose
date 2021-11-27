"""
OOP Review Exercise - Solutions
"""
from numpy import random


class Sphere:
    """
    sphere class
    """

    def __init__(self, radius):
        self.radius = radius

    def volume(self):
        """
        volume method
        """
        return (4 / 3) * 3.14 * self.radius ** 3

    def surface_area(self):
        """
        surface area method
        """
        return 4 * 3.14 * self.radius ** 2


class GuessingGame:
    """
    guessing game class
    """

    def __init__(self):
        self.rand_choice = random.randint(0, 10)

    def reset_random(self):
        """
        reset random method
        """
        print("Resetting Random Choice")
        self.rand_choice = random.randint(0, 10)

    def guess(self):
        """
        guess method
        """
        user_guess = int(input("Please input your guess (0-10): "))
        if user_guess == self.rand_choice:
            print("Correct Guess!")
        else:
            if user_guess < self.rand_choice:
                print("Sorry you didn't guess correctly!")
                print("Guess Higher!")
                print("Call the guess() method again to try again.")
            else:
                print("Sorry you didn't guess correctly!")
                print("Guess Lower!")
                print("Call the guess() method again to try again.")


def main():
    """
    main function
    """
    sphere = Sphere(1)
    print(sphere.surface_area())
    print(sphere.volume())
    guess = GuessingGame()
    print(guess.rand_choice)
    print(guess.reset_random())
    print(guess.guess())


if __name__ == "__main__":
    main()
