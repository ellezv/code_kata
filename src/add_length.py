"""Implementation of Add Length Kata on CodeWars."""


def add_length(str_):
    """Return a list with the length of each word added to each element."""
    arr = []
    for word in str_.split():
        arr.append(word + ' ' + str(len(word)))
    return arr
