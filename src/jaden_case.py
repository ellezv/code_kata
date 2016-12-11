"""Implementation of Jade Casing String Kata from Code Wars."""


def jaden_case(str_):
    """Return a capitalized string."""
    jaden_arr = [word.capitalize() for word in str_.split()]
    return ' '.join(jaden_arr)
