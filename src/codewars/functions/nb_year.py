def nb_year(p0: int, percent: float, aug: int, p: int) -> int:
    n: int = 0

    while p0 < p:
        p0 += int(p0 * percent / 100) + aug
        n += 1

    return n
