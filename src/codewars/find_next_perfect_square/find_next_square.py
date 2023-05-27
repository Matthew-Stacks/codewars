import doctest


def find_next_square(sq):
    """Return the next square if sq is a square, -1 otherwise

    :param sq: number to check
    :return: next square if sq is a square, -1 otherwise

    >>> find_next_square(121)
    144
    >>> find_next_square(625)
    676
    >>> find_next_square(65)
    -1
    >>> find_next_square(319225)
    320356
    >>> find_next_square(0)
    1
    """
    return -1 if sq**0.5 % 1 else int((sq**0.5 + 1) ** 2)


doctest.testmod()
