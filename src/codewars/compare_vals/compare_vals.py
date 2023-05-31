"""
    NAME:           cmp_x2o.py
    DESC:           Compares the number of `x` and `o` in string `s`.
    DIFFICULTY:     7kyu
    TAGS:           string, list, count, boolean
"""
import doctest


def cmp_x2o(s: str) -> bool:
    """Compares the number of `x` and `o` in string `s`.

    :param s: string to check
    :return: true if number of x's and o's are equal, false otherwise

    >>> cmp_vals("ooxx")
    true
    >>> xo("xooxx")
    false
    >>> xo("ooxXm")
    true
    >>> xo("zpzpzpp")
    true
    >>> xo("zzoo")
    false
    """
    return s.lower().count("x") == s.lower().count("o")


doctest.testmod()
