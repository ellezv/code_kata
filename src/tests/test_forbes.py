"""Tests for forbes kata."""

import json
with open('forbes.json') as data_file:
    DATA = json.load(data_file)

def test_get_oldest_youngest_returns_list():
    from forbes.py import get_oldest_and_youngest
    assert isinstance(get_oldest_and_youngest(DATA), list)
