"""Tests for is_vowel module."""
import pytest

NUM_TABLE = [
    [["a", 103, 110, 109, 104, 106], [97, 103, 110, 109, 104, 106]],
    [[107, 99, 110, 107, "e", 106, 112, 102], [107, 99, 110, 107, 101, 106, 112, 102]],
    [[100, 100, 116, "i", "u", 121], [100, 100, 116, 105, 117, 121]],
]


@pytest.mark.parametrize("result, input", NUM_TABLE)
def test_is_vow(result, input):
    """Test the is_vow function."""
    from is_vowel import is_vow
    assert is_vow(input) == result
