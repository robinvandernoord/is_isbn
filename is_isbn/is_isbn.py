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
    total = sum((index + 1) * int(value) for index, value in enumerate(isbn[::-1]))
    return total % 11 == 0


def check_isbn_13(isbn: str) -> bool:
    total = sum(
        int(value) * (3 if (index + 1) % 2 == 0 else 1)
        for index, value in enumerate(isbn[::-1])
    )
    return total % 10 == 0
