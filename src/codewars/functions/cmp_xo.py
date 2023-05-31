"""
    NAME:           cmp_xo.py
    DESC:           Compares the number of `x` and `o` in string `s`.
    DIFFICULTY:     7kyu
    TAGS:           string, list, count, boolean
"""
import doctest


def cmp_xo(s: str) -> bool:
    """Compares the number of `x` and `o` in string `s`.

    :param s: string to check
    :return: true if number of x's and o's are equal, false otherwise

    >>> cmp_xo("ooxx")
    true
    >>> cmp_xo("xooxx")
    false
    >>> cmp_xo("ooxXm")
    true
    >>> cmp_xo("zpzpzpp")
    true
    >>> cmp_xo("zzoo")
    false
    """
    return s.lower().count("x") == s.lower().count("o")


doctest.testmod()
