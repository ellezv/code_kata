"""Test for lightsaber module."""
import pytest


NAME_TABLE = [
    ["Zach", 18],
    ["Somebody else", 0],
    ["", 0],
]


@pytest.mark.parametrize("name, number", NAME_TABLE)
def test_num_lightsaber(name, number):
    """Test num_lightsaber function."""
    from lightsaber import num_lightsaber
    assert num_lightsaber(name) == number
