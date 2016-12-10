"""Test for get_average module."""
import pytest


MARKS_TABLE = [
    [[2, 2, 2, 2], 2],
    [[10, 20, 30], 20],
    [[1, 5, 87, 45, 8, 8], 25],
    [[1, 2, 15, 15, 17, 11, 12, 17, 17, 14, 13, 15, 6, 11, 8, 7], 11]
]


@pytest.mark.parametrize("marks, result", MARKS_TABLE)
def test_average(marks, result):
    """Test get_average function."""
    from get_average import get_average
    assert get_average(marks) == result
