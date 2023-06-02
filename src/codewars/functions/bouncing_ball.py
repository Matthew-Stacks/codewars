import doctest


def bouncing_ball(h: float, bounce: float, window: float) -> int:
    """Determine how many times a ball dropped from height `h`
    will be seen from a window with height `window`.

    Bouncing means:
    - the ball moves from the ground toward the window. In this case, `h` must exceed `window`;
    - the ball moves from the window toward the ground.

    If constraints are not respected, return -1.

    :param h: original height from which the ball was dropped
    :param bounce: coefficient of restitution
    :param window: height of the window
    :return: number of times the ball will be seen from the window
    :constraints: h > window > 0., 1. > bounce > 0.

    >>> bouncing_ball(3, 0.66, 1.5)
    3
    >>> bouncing_ball(30, 0.66, 1.5)
    15
    >>> bouncing_ball(3, 1, 1.5)
    -1
    """
    ground: float = 0.0
    abs_bounce_floor: float = 0.0
    abs_bounce_ceil: float = 1.0
    if not (h > window > ground and abs_bounce_ceil > bounce > abs_bounce_floor):
        return -1

    ball_seen: int = 0
    while h > window:
        ball_seen += 1
        h *= bounce
        if h > window:
            ball_seen += 1

    return ball_seen


doctest.testmod()
