"""Test for the add_length module."""
import pytest

STR_TABLE = [
    ["Hello Goodbye", ["Hello 5", "Goodbye 7"]],
    ["this is a good test", ["this 4", "is 2", "a 1", "good 4", "test 4"]],
    ["one", ["one 3"]],
    ["", []]
]


@pytest.mark.parametrize("string, result", STR_TABLE)
def test_add_length(string, result):
    """Test for add_length function."""
    from add_length import add_length
    assert add_length(string) == result
