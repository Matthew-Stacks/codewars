def xo(s: str) -> bool:
    """
    :param s: string to check
    :return: true if number of x's and o's are equal, false otherwise

    >>> xo("ooxx")
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
