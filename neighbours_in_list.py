def count_neighbours(lst: list[int]) -> int:
    """
    Count the number of neighbours in a list.
    A neighbour is defined as two consecutive integers in the list that differ by 1.

    Args:
        lst (list[int]): A list of integers.

    Returns:
        int: The number of neighbours in the list.
    """
    list_index = 0
    count = 0
    best = 0
    while list_index < (len(lst) - 1):
        if lst[list_index] - lst[list_index + 1] == 1 or lst[list_index + 1] - lst[list_index] == 1:
            count += 1
        else:
            if count > best:
                best = count
            count = 0
        list_index += 1
    return best + 1 


def main():
    lista = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(count_neighbours(lista))


if __name__ == "__main__":
    main()