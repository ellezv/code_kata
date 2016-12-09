"""Implementation of Is There a Vowel in There Kata on Code Wars."""


def is_vow(lst):
    """Replace an int in list if it's a vowel ascii code."""
    vow = {97: 'a', 101: 'e', 105: 'i', 111: 'o', 117: 'u'}
    new_lst = []
    for word in lst:
        if word in vow.keys():
            word = vow[word]
        new_lst.append(word)
    return new_lst
