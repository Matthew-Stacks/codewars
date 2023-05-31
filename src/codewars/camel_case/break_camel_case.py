"""
    NAME:           break_camel_case.py
    DESC:           This file contains a function that converts a string to camel case.
    DIFFICULTY:     6kyu
    TAGS:           string, case, camelcase
"""


def break_camel_case(s: str) -> str:
    """
    :param s: string to break
    :return: broken string

    >>> break_camel_case("camelCasing")
    "camel Casing"
    >>> break_camel_case("camelCasingTest")
    "camel Casing Test"
    >>> break_camel_case("")
    ""
    >>> break_camel_case("camelcasingtest")
    "camelcasingtest"
    >>> break_camel_case("CamelCasingtest")
    "Camel Casingtest"
    """
    return "".join(" " + c if c.isupper() else c for c in s)
