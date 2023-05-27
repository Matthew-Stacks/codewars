import doctest


def to_camel_case(text: str) -> str:
    """Convert `text` to camel case.

    :param text: string to convert
    :return: converted string

    >>> to_camel_case('')
    ''
    >>> to_camel_case('one_two_three')
    'oneTwoThree'

    >>> to_camel_case('one-two-three')
    'oneTwoThree'

    >>> to_camel_case('one_two-three')
    'oneTwoThree'

    >>> to_camel_case('one-two_three')
    'oneTwoThree'

    >>> to_camel_case('One_Two_Three')
    'OneTwoThree'

    >>> to_camel_case('One-Two-Three')
    'OneTwoThree'

    >>> to_camel_case('One_Two-Three')
    'OneTwoThree'

    >>> to_camel_case('One-Two_Three')
    'OneTwoThree'
    """
    if not text:
        return text

    text = text.replace("-", "_")
    text = text.split("_")

    return text[0] + "".join([word.capitalize() for word in text[1:]])


doctest.testmod()
