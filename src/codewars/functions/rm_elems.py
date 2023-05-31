import doctest


def rm_elems(array: list[int], n: int) -> list[int]:
    """Remove elements that appear more than `n` times from `array`.
    Remove the rightmost duplicates first.
    For example, if `n` is 2, then keep only the first 2 occurrences of each element.

    :param array: list[int]
    :param n: int
    :return: list[int]

    >>> rm_elems([1, 2, 2, 3], 1)
    [1, 2, 3]
    >>> rm_elems([1, 2, 2, 1, 2, 4, 2, 3, 5, 2, 2, 2, 2], 3)
    [1, 2, 2, 1, 2, 4, 3, 5]
    >>> rm_elems([1, 1], 1)
    [1]
    >>> rm_elems([1, 2, 3, 4, 5, 6, 7, 8, 9], 0)
    []
    """
    result = []
    for i in array:
        if result.count(i) < n:
            result.append(i)
    return result


doctest.testmod()
