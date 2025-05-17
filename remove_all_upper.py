def remove_upper(lst: list[str]) -> list[str]:
    """
    Remove all elements from a list that are all uppercase.
    """
    return [string for string in lst if not string.isupper()]


def main() -> None:
    """
    Main function to execute the program.
    """
    jono = ["ABC", "def", "ISO", "TOINENISO", "pieni", "toinen pieni", "Osittain Iso"]
    print(f"{remove_upper(jono)}")


if __name__ == "__main__":
    main()