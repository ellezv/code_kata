"""Implementation of Title Case Kata on Code Wars."""


def title_case(title, minor_words=''):
    """Return a string of capitalized words with the exception of optional minor words."""
    if title == '':
        return ''
    else:
        title_list = title.lower().split()
        minor_list = minor_words.lower().split()
        final_list = []
        for word in title_list:
            if word.lower() in minor_list:
                final_list.append(word)
            else:
                final_list.append(word.capitalize())
        final_list[0] = title_list[0].title()
        return ' '.join(final_list)
