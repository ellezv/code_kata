"""Implementation of get average kata on Code Wars."""
import math


def get_average(marks):
    """Return the list average."""
    return math.floor(sum(marks) / len(marks))
