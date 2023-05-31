import doctest


def square_digits(num: int) -> int:
    """For each digit in `num`, square that digit and convert to type str.
    Once all digits have been squared, join them together and convert to type int.

    :param num: number to square digits of
    :return: squared numbers joined together

    >>> square_digits(0)
    0
    >>> square_digits(1)
    1
    >>> square_digits(12)
    14
    >>> square_digits(123)
    149
    >>> square_digits(1234)
    14916
    >>> square_digits(9119)
    811181
    """
    return int("".join(str(int(d) ** 2) for d in str(num)))


doctest.testmod()
