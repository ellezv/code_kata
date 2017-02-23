"""Tests for the sort_cards module."""

import pytest


DECKS = [
    [list('39A5T824Q7J6K'), list('A23456789TJQK')],
    [list('Q286JK395A47T'), list('A23456789TJQK')],
    [list('54TQKJ69327A8'), list('A23456789TJQK')],
    [list('JKQT'), list('TJQK')],
    [list('543792'), list('234579')],
]


@pytest.mark.parametrize("deck, sorted", DECKS)
def test_sort_cards(deck, sorted):
    """Test sort_cards returns an appropriately sorted deck."""
    from sort_cards import sort_cards
    assert sort_cards(deck) == sorted
