import doctest


def rm_chars(s: str) -> str:
    """Remove first and last characters from string `s`.

    :param s: string to remove characters from
    :return: string with first and last characters removed

    >>> rm_chars('')
    ''
    >>> rm_chars('a')
    ''
    >>> rm_chars('ab')
    ''
    >>> rm_chars('abc')
    'b'
    >>> rm_chars('abcd')
    'bc'
    >>> rm_chars('abcde')
    'bcd'
    """
    return s[1:-1]


doctest.testmod()
