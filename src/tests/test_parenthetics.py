"""Tests for proper_parenthetics module."""

import pytest


PARENS = [
    [')))(((', -1],
    [')', -1],
    ['(', 1],
    ['(())', 0],
    ['(9())', 0],
]


@pytest.mark.parametrize("iter, result", PARENS)
def test_is_balanced(iter, result):
    """Test the expected value is returned when is_balanced is called."""
    from proper_parenthetics import Queue
    queue = Queue(iter)
    assert queue.is_balanced() == result
