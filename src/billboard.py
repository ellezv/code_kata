"""Implementation of Name on Billboard Kata on CodeWars"""
from numpy import multiply


def billboard(name, price=30):
    """Return cost of printing name on billboard."""
    return multiply(len(name), price)
