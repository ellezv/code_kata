"""Implementation of Simple Pig Latin Kata from Code Wars."""


def pig_it(text):
    """Return a string a piglatin string."""
    lst = []
    for word in text.split():
        if word == '!' or word == '?':
            lst.append(word)
        else:
            word = word[1:] + word[0] + 'ay'
            lst.append(word)
    return ' '.join(lst)
