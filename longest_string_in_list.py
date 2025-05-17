def longest_string(lst: list[str]) -> tuple[str, int]:
    """
    This function takes a list of strings as input and returns the longest string from the list.
    
    :param lst: List of strings
    :return: tuple with longest string and its length
    """
    longest = lst[0]
    lenght = len(longest)
    for string in lst:
        if len(string) > lenght:
            longest = string
            lenght = len(longest)
    return (longest, lenght)

def main() -> None:
    """
    Main function to execute the program.
    """
    lista1 = ["eka", "toka", "kolmas", "seitsemäs"]
    lista2 = ["pekka", "emilia", "venla", "eero", "antti", "juhani"]

    pisin_merkkijono1, pituus1 = longest_string(lista1)
    pisin_merkkijono2, pituus2 = longest_string(lista2)

    print(f"Lista 1: pisin merkkijono on {pisin_merkkijono1} ja sen pituus on {pituus1} merkkiä")
    print(f"Lista 2: pisin merkkijono on {pisin_merkkijono2} ja sen pituus on {pituus2} merkkiä")


if __name__ == "__main__":
    main()