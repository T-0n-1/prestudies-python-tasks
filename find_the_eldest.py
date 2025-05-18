def find_oldest(people: list[tuple[str, int]]) -> str:
    """
    This function takes a list of tuples representing people with their birth year and returns the name of the oldest person.
    
    :param: List of tuples, where each tuple contains name and birth year.
    :return: The name of the oldest person.
    """
    oldest_person = min(people, key=lambda person: person[1])
    return oldest_person[0]


h1 = ("Arto", 1977)
h2 = ("Einari", 1985)
h3 = ("Maija", 1953)
h4 = ("Essi", 1997)
hlista = [h1, h2, h3, h4]

print(find_oldest(hlista))