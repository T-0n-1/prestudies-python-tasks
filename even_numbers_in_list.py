def list_with_even_numbers(list: list[int]) -> list[int]:
    """
    Returns a new list containing only the even numbers from the given list.
    
    Args:
        list: A list of integers.
    
    Returns:
        A new list containing only the even numbers from the input list.
    """
    return [number for number in list if number % 2 == 0]


def print_lists(list: list[int]) -> None:
    """
    Prints the original list and the list with even numbers.
    
    Args:
        list: A list of integers.
    """
    print(f"Alkuperäinen {list}")
    print(f"uusi {list_with_even_numbers(list)}")


def main() -> None:
    """
    Main function to execute the program.
    """
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print_lists(numbers)


if __name__ == "__main__":
    main()