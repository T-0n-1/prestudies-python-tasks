from re import search


def find_movies(movies: list[dict], search: str) -> list[dict]:
    """
    Find movies that contain the search term in registry.

    Args:
        movies (list[dict]): A list of movie dictionaries.
        search (str): The search term.

    Returns:
        list[dict]: A list of movies that match the search term.
    """
    return [
        movie for movie in movies
        if search.lower() in movie['nimi'].lower()
    ]


rekisteri = [{"nimi": "Pythonin viemää", "ohjaaja": "Pekka Python", "vuosi": 2017, "pituus": 116},
{"nimi": "Python lentokoneessa", "ohjaaja": "Renny Pythonen", "vuosi": 2001, "pituus": 94},
{"nimi": "Koodaajien yö", "ohjaaja": "M. Night Python", "vuosi": 2011, "pituus": 101}]

lista = find_movies(rekisteri, "python")
print(lista)