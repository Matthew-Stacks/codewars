import doctest


def return_char(chars: list[str]) -> str:
    """Return the missing character from an ordered list of characters.

    :param chars: list[str]
    :return: str

    >>> return_char(['a', 'b', 'c', 'd', 'f'])
    'e'

    >>> return_char(['O', 'Q', 'R', 'S'])
    'P'

    >>> return_char(['a', 'b', 'c', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l'])
    'd'

    >>> return_char(['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L'])
    'B'

    >>> return_char([])
    ''
    """
    if not chars:
        return ""

    left_pointer: int = 0
    right_pointer: int = len(chars) - 1
    midpoint: int = left_pointer + (right_pointer - left_pointer) // 2
    char_vals: list[int] = [ord(c) for c in chars]

    while left_pointer < midpoint:
        if char_vals[left_pointer] + 1 != char_vals[left_pointer + 1]:
            return chr(char_vals[left_pointer] + 1)
        left_pointer += 1

    while right_pointer >= midpoint:
        if char_vals[right_pointer] - 1 != char_vals[right_pointer - 1]:
            return chr(char_vals[right_pointer] - 1)
        right_pointer -= 1


doctest.testmod()
