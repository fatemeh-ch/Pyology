"""
Program: Check if a number is positive, negative, or zero.
Author: Fatemeh
Description: Takes a user input, validates it, and determines the sign of the number.
"""


class EmptyFieldError(Exception):
    pass


def check_number(number):
    if number > 0:
        print(f"{number} is positive")
    elif number < 0:
        print(f"{number} is negative")
    else:
        print("The number is zero")


try:
    user_input = input("Please enter your number: ").strip()
    if not user_input:
        raise EmptyFieldError("You have to enter something")

    number = float(user_input)
    check_number(number)

except ValueError:
    print("You must enter a valid number.")
except EmptyFieldError as error:
    print(error)
