import doctest


def rm_char(s: str) -> str:
    """Remove first and last characters from string `s`.

    :param s: string to remove characters from
    :return: string with first and last characters removed

    >>> remove_char('')
    ''
    >>> remove_char('a')
    ''
    >>> remove_char('ab')
    ''
    >>> remove_char('abc')
    'b'
    >>> remove_char('abcd')
    'bc'
    >>> remove_char('abcde')
    'bcd'
    """
    return s[1:-1]


doctest.testmod()
