import doctest


def find_uniq_str(arr: list[str]) -> str:
    a, b = set(arr)
    return a if arr.count(a) == 1 else b


doctest.testmod()
