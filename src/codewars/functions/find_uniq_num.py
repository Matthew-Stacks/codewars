import collections
import doctest


def find_uniq_num(arr: list[int | float]) -> int | float:
    """Return the unique number in the array.

    :param arr: list of numbers
    :return: unique number in the array
    :constraints: 3 <= arr.length < 2^31 - 1

    >>> find_uniq_num([1, 1, 1, 2, 1, 1])
    2
    >>> find_uniq_num([0, 0, 0.55, 0, 0])
    0.55
    >>> find_uniq_num([3, 10, 3, 3, 3])
    10
    >>> find_uniq_num([3, 3, 3, 3, 3, 10, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3])
    10
    >>> find_uniq_num([3., 3., 3., 3., 3., 10.])
    10.0
    >>> find_uniq_num([3., 3., 3, 3, 1])
    1
    """
    counter = collections.Counter(arr)
    return counter.most_common()[-1][0]


doctest.testmod()
