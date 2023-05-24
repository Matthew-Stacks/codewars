def well(x):
    good_ideas = x.count("good")
    match good_ideas:
        case n if n <= 0:
            return "Fail!"
        case n if 0 < n < 3:
            return "Publish!"
        case n:
            if n >= 3:
                return "I smell a series!"
    return -1
