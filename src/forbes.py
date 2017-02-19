"""Implementation of the forbes Kata."""


def get_oldest_and_youngest(data):
    """Find oldest billionaire under 80 and youngest billionaire with valid age."""
    oldest_person = data[0]
    youngest_person = data[0]
    for person in data:
        if person['age'] < 80 and person['age'] > 0:
            if person['age'] > oldest_person['age']:
                oldest_person = person
            if person['age'] < youngest_person['age']:
                youngest_person = person
    output = """
    Oldest Billionaire is {}, {} $ net worth, {}.
    Youngest Billionaire is {}, {} $ net worth, {}.
    """.format(
        oldest_person["name"],
        oldest_person["net_worth (USD)"],
        oldest_person["source"],
        youngest_person["name"],
        youngest_person["net_worth (USD)"],
        youngest_person["source"])
    return output


if __name__ == '__main__':
    import json
    with open('forbes.json') as data_file:
        the_data = json.load(data_file)
    print(get_oldest_and_youngest(the_data))
