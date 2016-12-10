"""Implementation of Opposites attract on Code Wars."""


def lovefunc(flower1, flower2):
    """Return true if one number is odd and the other is not."""
    if not flower1 % 2 and flower2 % 2:
        return True
    elif not flower2 % 2 and flower1 % 2:
        return True
    return False
