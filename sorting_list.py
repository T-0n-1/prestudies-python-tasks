original_list: list[int] = []


def sort_list(list: list) -> list:
    """
    Sort the list in ascending order.
    """
    return sorted(list)


def add_to_list(list: list, number: int) -> list:
    """
    Add a new element to the list.
    """
    list.append(number)
    return list


def prompt_for_number() -> int:
    """
    Ask the user for a number.
    """
    return int(input("Anna luku: "))


def main() -> None:
    """
    Main function to execute the program.
    """
    while True:
        luku = prompt_for_number()
        if luku != 0:
            add_to_list(original_list, luku)
            print(f"Lista: {original_list}")
            print(f"Järjestettynä: {sorted(original_list)}")
        else:
            print("Moi!")
            break


if __name__ == "__main__":
    main()