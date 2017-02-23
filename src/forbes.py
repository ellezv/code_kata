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
    return [oldest_person, youngest_person]


if __name__ == '__main__':  # pragma: no cover
    import json
    with open('forbes.json') as data_file:
        the_data = json.load(data_file)

    persons = get_oldest_and_youngest(the_data)
    output = """
    Oldest Billionaire is {}, {} $ net worth, {}.
    Youngest Billionaire is {}, {} $ net worth, {}.
    """.format(
        persons[0]["name"],
        persons[0]["net_worth (USD)"],
        persons[0]["source"],
        persons[1]["name"],
        persons[1]["net_worth (USD)"],
        persons[1]["source"])
    print(output)
