import doctest


def gen_hashtag(s: str) -> str | bool:
    """Generate hashtag from string.

    param s: string to generate hashtag from
    return: generated hashtag
    constraints: 1 <= len(s) <= 140

    >>> gen_hashtag('')
    False
    >>> gen_hashtag(f'HelloWorldHelloWorldHelloWorldHelloWorldHelloWorldHelloWorld'+
    'HelloWorldHelloWorldHelloWorldHelloWorldHelloWorldHelloWorldHelloWorldHelloWorld!')
    False
    >>> gen_hashtag('Do We have A Hashtag')
    '#DoWeHaveAHashtag'
    >>> gen_hashtag('Codewars')
    '#Codewars'
    """
    hashtag_max_len: int = 140
    if not s or len(s) > hashtag_max_len:
        return False

    return "#" + "".join(word.capitalize() for word in s.split())


doctest.testmod()
