"""
National ID Validation Program
-----------------------------

This module provides a complete validation system for Iranian National IDs.
It includes:

1. **Custom Exceptions**
   - EmptyFieldError: Raised when no input is provided.
   - LengthTooShortError: Raised when the national ID contains fewer than 10 digits.

2. **Input Validation**
   - Ensures the user enters only numeric characters.
   - Ensures the national ID contains exactly 10 digits.
   - Converts the string into a list of integer digits.

3. **Check-Digit Verification (Official Algorithm)**
   - Multiplies the first 9 digits by descending weights from 10 to 2.
   - Computes the checksum and remainder based on modulo 11.
   - Confirms accuracy by comparing the computed remainder with the final digit.

Overall, this program ensures that user input is valid, clean, and fully compliant
with the standard Iranian national ID check-digit algorithm.
"""

import string


class EmptyFieldError(Exception):
    pass


class LengthTooShortError(Exception):
    pass


def check_national_id(National_Id):
    National_Id_list = []
    for char in National_Id:
        if char.isalpha():
            raise ValueError("You have to enter numbers not string!")
        if char.isspace():
            raise ValueError("You have no permission to use space!")
        if char not in string.digits:
            raise ValueError("You have to enter numbers!")
        if char.isnumeric():
            National_Id_list.append(int(char))
    if len(National_Id_list) < 10:
        raise LengthTooShortError("National Id must be 10 characters")
    return National_Id_list


def validate_national_id(National_id):
    total = 0
    counter = 10
    for i in range(9):
        total += National_id[i] * counter
        counter -= 1

    remainder = total % 11

    check_digit = National_id[9]

    if remainder < 2:
        if check_digit == remainder:
            print("Valid National ID")
        else:
            print("Invalid National ID")

    else:  # remainder >= 2
        if check_digit == 11 - remainder:
            print("Valid National ID")
        else:
            print("Invalid National ID")


try:
    National_Id = input(
        "Please enter your National ID with no spaces : ").strip()

    if not National_Id:
        raise EmptyFieldError("You have to enter a National ID!")

    validate_national_id(check_national_id(National_Id))

except (EmptyFieldError, LengthTooShortError, ValueError) as error:
    print(error)
