def all_reversed(lst: list[str]) -> list[str]:
    """
    Reverse the order of elements in a list and order of chars in each element.
    
    Args:
        lst (list): The list to reverse.
        
    Returns:
        list: A new list with the elements and chars in reverse order.
    """
    return [element[::-1] for element in lst][::-1]


def main() -> None:
    """
    Main function to execute the program.
    """
    lista = ["Moi", "kaikki", "esimerkki", "vielä yksi"]
    print(all_reversed(lista))


if __name__ == "__main__":
    main()