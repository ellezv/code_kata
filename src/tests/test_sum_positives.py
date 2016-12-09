"""Tests for our sum_positives module."""
import pytest

LIST_TABLE = [
    [[1, 2, 3, 4, 5], 15],
    [[1, -2, 3, 4, 5], 13],
    [[-1, 2, 3, 4, -5], 9],
    [[-1, -4, -7], 0]
]


@pytest.mark.parametrize("lst, result", LIST_TABLE)
def test_sum_positives(lst, result):
    """Test our sum_positives function."""
    from sum_positives import sum_positives
    assert sum_positives(lst) == result
