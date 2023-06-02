import doctest


def snail(snail_map: list[list[int]]) -> list[int] | None:
    """Given an n x n array `snail_map`, return an array with dimensions 1 x (n ** 2).
    Arrange the transformed array by placing the outermost elements leftmost in the new array.
    Work clockwise towards the center.
    Because all valid inputs are n x n squares, the center element of the input array
    will be the last and rightmost element of the output array.

    :param snail_map: A square array of integers.
    :return: A flattened array of integers.

    >>> snail([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    [1, 2, 3, 6, 9, 8, 7, 4, 5]
    >>> snail([[1, 2, 3], [8, 9, 4], [7, 6, 5]])
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> snail([[]])
    []
    >>> snail([[1]])
    [1]
    >>> snail([[1, 2], [3, 4]])
    [1, 2, 4, 3]
    """
    if not snail_map:
        return None

    snail_list = []
    while snail_map:
        # Add the first row to the snail list.
        snail_list.extend(snail_map.pop(0))

        # Add the last element of each row to the snail list.
        for row in snail_map:
            snail_list.append(row.pop())

        # Add the last row in reverse order to the snail list.
        if snail_map:
            snail_list.extend(snail_map.pop()[::-1])

        # Add the first element of each row in reverse order to the snail list.
        for row in snail_map[::-1]:
            snail_list.append(row.pop(0))

    return snail_list


doctest.testmod()
