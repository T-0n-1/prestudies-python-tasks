def uniques_in_list(lst: list[int]) -> list[int]:
    """
    This function takes a list as input and returns a new list containing only the unique elements from the original list.
    
    :param lst: List of elements
    :return: List of unique elements
    """
    return list(set(lst))

def main() -> None:
    lista = [3, 2, 2, 1, 3, 3, 1]
    print(uniques_in_list(lista))


if __name__ == "__main__":
    main()