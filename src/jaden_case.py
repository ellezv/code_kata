"""Implementation of Jade Casing String Kata from Code Wars."""


def jaden_case(str_):
    jaden_arr = []
    for word in str_.split():
        word = word.capitalize()
        jaden_arr.append(word)
    return ' '.join(jaden_arr)
