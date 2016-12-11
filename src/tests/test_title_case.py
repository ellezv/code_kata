"""Test for title_case module."""
import pytest


BOOK_TABLE = [
    ['a clash of KINGS', 'a an the of', 'A Clash of Kings'],
    ['THE WIND IN THE WILLOWS', 'The In', 'The Wind in the Willows'],
    ['the slow Regard of silent THINGS', 'of', 'The Slow Regard of Silent Things'],
    ['', '', '']
]


@pytest.mark.parametrize("book, minor_words, result", BOOK_TABLE)
def test_title_case(book, minor_words, result):
    """Test for title_case function."""
    from title_case import title_case
    assert title_case(book, minor_words) == result
