"""Implementation of the Kata Sum of Positive."""


def sum_positives(lst):
    """Return the sum of positive number in list."""
    return sum([num for num in lst if num > 0])
