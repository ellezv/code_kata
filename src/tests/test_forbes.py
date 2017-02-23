"""Tests for forbes kata."""

import pytest
import json
from six import string_types
with open('src/forbes.json') as data_file:
    DATA = json.load(data_file)


@pytest.fixture
def oldest():
    """Return the oldest billionaire from the function."""
    from forbes import get_oldest_and_youngest
    return get_oldest_and_youngest(DATA)[0]


@pytest.fixture
def youngest():
    """Return the younget billionaire from the function."""
    from forbes import get_oldest_and_youngest
    return get_oldest_and_youngest(DATA)[1]


def test_get_oldest_youngest_returns_list_of_2():
    """Test that the function returns a list of two items."""
    from forbes import get_oldest_and_youngest
    assert isinstance(get_oldest_and_youngest(DATA), list)
    assert len(get_oldest_and_youngest(DATA)) == 2


def test_get_oldest_under_80(oldest):
    """Test the function returns a person under 80."""
    assert oldest["age"] < 80


def test_get_youngest_valid_age(youngest):
    """Test the function returns a person with a valid age."""
    assert youngest["age"] > 0


def test_oldest_has_name(oldest):
    """Test the function return the oldest billionaire's name."""
    assert isinstance(oldest["name"], string_types)
    assert len(oldest["name"]) > 2


def test_youngest_has_name(youngest):
    """Test the function return the youngest billionaire's name."""
    assert isinstance(youngest["name"], string_types)
    assert len(youngest["name"]) > 2


def test_oldest_has_industry(oldest):
    """Test the function returns a person with an industry."""
    assert isinstance(oldest["source"], string_types)
    assert len(oldest["source"]) > 2


def test_youngest_has_industry(youngest):
    """Test the function returns a person with an industry."""
    assert isinstance(youngest["source"], string_types)
    assert len(youngest["source"]) > 2


def test_oldest_has_net_worth(oldest):
    """Test the function returns a person with a networth above a billion."""
    assert int(oldest["net_worth (USD)"]) > 1000000000


def test_youngest_has_net_worth(youngest):
    """Test the function returns a person with a networth."""
    assert int(youngest["net_worth (USD)"]) > 1000000000
