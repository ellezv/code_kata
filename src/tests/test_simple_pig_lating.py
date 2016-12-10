"""Test for simple_pig_latin module."""
import pytest


STR_TABLE = [
    ['Pig latin is cool', 'igPay atinlay siay oolcay'],
    ['This is my string', 'hisTay siay ymay tringsay']
]


@pytest.mark.parametrize("input, output", STR_TABLE)
def test_pig_it(input, output):
    """Test pig_it function."""
    from simple_pig_latin import pig_it
    assert pig_it(input) == output
