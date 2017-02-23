"""An implementation of the Sort Deck of Cards kata on Codewars."""


def sort_cards(cards):
    """Sort shuffled list of cards, sorted by rank."""
    priority = {
        "A": 0, "2": 1, "3": 2, "4": 3, "5": 4, "6": 5, "7": 6, "8": 7,
        "9": 8, "T": 9, "J": 10, "Q": 11, "K": 12
    }
    return sorted(cards, key=lambda x: priority[x])
