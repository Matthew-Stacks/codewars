import doctest


def square_digits(num: int) -> int:
    """For each digit in `num`, square it and return the result as a string.
    >>> square_digits(9119)
    811181
    """
    return int("".join(str(int(d) ** 2) for d in str(num)))


doctest.testmod()
