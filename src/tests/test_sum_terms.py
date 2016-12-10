"""Tests for sum_terms module."""
import pytest

NUM_TABLE = [
    [1, "1.00"],
    [2, "1.25"],
    [3, "1.39"],
    [5, "1.57"]
]


@pytest.mark.parametrize("n, result", NUM_TABLE)
def test_sum_terms(n, result):
    """Test sum_terms function."""
    from sum_terms import series_sum
    assert series_sum(n) == result
