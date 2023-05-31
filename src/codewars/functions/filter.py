def well(x: list[str]) -> str | int:
    series_min: int = 3
    good_ideas = x.count("good")

    match good_ideas:
        case n if n <= 0:
            return "Fail!"
        case n if 0 < n < series_min:
            return "Publish!"
        case n if n >= series_min:
            return "I smell a series!"
        case _:
            return -1
