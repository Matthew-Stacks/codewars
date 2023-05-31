def duplicate_encode(word: str) -> str:
    """
    :param word: string to encode
    :return: encoded string

    >>> duplicate_encode("din")
    "((("
    >>> duplicate_encode("recede")
    "()()()"
    >>> duplicate_encode("Success")
    ")())())"
    >>> duplicate_encode("(( @")
    "))(("
    """
    word = word.lower()
    return "".join("(" if word.count(c) == 1 else ")" for c in word)
