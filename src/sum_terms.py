"""Implementation of Sum of nth Term Kata on Code Wars."""
from __future__ import division


def series_sum(n):
    """Return nth value in series."""
    if n <= 1:
        return "%.2f" % n
    count = 1
    for num in range(n - 1):
        n -= 1
        count += 1 / (3 * n + 1)
    return "%.2f" % count
