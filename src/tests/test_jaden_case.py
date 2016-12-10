"""Test for jaden_case module."""


def test_jaden_case():
    """Test jaden case function."""
    from jaden_case import jaden_case
    st = "How can mirrors be real if our eyes aren't real"
    assert jaden_case(st) == "How Can Mirrors Be Real If Our Eyes Aren't Real"
