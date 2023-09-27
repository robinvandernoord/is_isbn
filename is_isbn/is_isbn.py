# -*- coding: utf-8 -*-

"""Main module."""


def is_isbn(isbn: str) -> bool:
    """
    Check if a given ISBN is valid.

    Input type is str.
    In other cases the function will attempt to convert provided argument to a str.
    In case of an error the return value will be False.

    Returns either True or False depending on the result.
    """

    # Test ISBN must be provided as a string
    if not isinstance(isbn, str):
        try:
            isbn = str(isbn)
        except:
            return False

    # Clean the test string of any delimiters, typos or spaces if they exist.
    isbn = "".join(filter(str.isdigit, isbn))

    # ISBN must be either 10 or 13 characters long
    if len(isbn) == 10:
        return check_isbn_10(isbn)
    elif len(isbn) == 13:
        return check_isbn_13(isbn)
    else:
        return False


def check_isbn_10(isbn: str) -> bool:
    """
    Check if a given ISBN-10 (International Standard Book Number) is valid.

    This function calculates whether it is valid based on the following criteria:

    1. Multiply each digit by its position (1-based index) from right to left.
    2. Sum the results of these multiplications.
    3. If the sum is divisible by 11, the ISBN-10 is considered valid.

    Args:
        isbn (str): The ISBN-10 string to be checked.

    Returns:
        bool: True if the ISBN-10 is valid, False otherwise.
    """
    total = sum((index + 1) * int(value) for index, value in enumerate(isbn[::-1]))
    return total % 11 == 0


def check_isbn_13(isbn: str) -> bool:
    """
    Check if a given ISBN-13 (International Standard Book Number) is valid.

    This function calculates whether it is valid based on the following criteria:

    1. Multiply each digit by 3 if its position (1-based index) from right to left is even,
       otherwise multiply by 1.
    2. Sum the results of these multiplications.
    3. If the sum is divisible by 10, the ISBN-13 is considered valid.

    Args:
        isbn (str): The ISBN-13 string to be checked.

    Returns:
        bool: True if the ISBN-13 is valid, False otherwise.
    """
    total = sum(
        int(value) * (3 if (index + 1) % 2 == 0 else 1)
        for index, value in enumerate(isbn[::-1])
    )
    return total % 10 == 0
