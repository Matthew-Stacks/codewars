def spin_words(sentence):
    words: list[str] = sentence.split()
    spin_value: int = 5
    for i in range(len(words)):
        if len(words[i]) >= spin_value:
            words[i] = words[i][::-1]
    return " ".join(words)
