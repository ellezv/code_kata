"""Test for module opposites."""
import pytest


FLOWER_TABLE = [
    [2, 3, True],
    [2, 2, False],
    [3, 3, False],
    [5, 6, True]
]


@pytest.mark.parametrize("int1, int2, result", FLOWER_TABLE)
def test_opposites(int1, int2, result):
    """Test opposites function."""
    from opposites import lovefunc
    assert lovefunc(int1, int2) == result
