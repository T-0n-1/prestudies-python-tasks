from re import fullmatch


def index_of_smallest_mean(means: list) -> int:
    """
    Find the index of the contestant with the smallest mean score.

    :param means: list of means of the scores.
    :return: index of the contestant with the smallest mean score.
    """
    if not means:
        raise ValueError("Means list cannot be empty")
    return means.index(min(means))


def smallest_mean(*contestants) -> dict:
    """
    Calculate the means of the contestant's scores.

    :param contestants: dictionaries containing the contestant and his/her scores.
    :return: dict of the contestant with the smallest mean of the scores.
    """
    means = []
    for contestant in contestants:
        if not isinstance(contestant, dict):
            raise TypeError("Contestant must be a dictionary")
        tulos_values = [value for key, value in contestant.items() if fullmatch(r"tulos\d+", key)]
        mean = sum(tulos_values) / len(tulos_values)
        means.append(mean)
    index = index_of_smallest_mean(means)
    return contestants[index]


def main():
    """
    Main function to run the program.
    """
    henkilo1 = {"nimi": "Keijo", "tulos1": 2, "tulos2": 3, "tulos3": 3}
    henkilo2 = {"nimi": "Reijo", "tulos1": 5, "tulos2": 1, "tulos3": 8}
    henkilo3 = {"nimi": "Veijo", "tulos1": 3, "tulos2": 1, "tulos3": 1}
    print(smallest_mean(henkilo1, henkilo2, henkilo3))


if __name__ == "__main__":
    main()