"""Tests for billboard module."""


def test_billboard_with_opt():
    """Test billboard function with optional argument."""
    from billboard import billboard
    assert billboard("Hadufuns John", 20) == 260


def test_billboard_no_opt():
    """Test billboard method with no optional argument."""
    from billboard import billboard
    assert billboard("Abishai Charalampos") == 570
