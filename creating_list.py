def ask_for_numbers() -> list[int]:
    """
    Ask the user for a list of integers.

    Returns:
        A list of integers entered by the user.
    """
    list_of_numbers = []
    numbers = int(input("Kuinka monta numeroa: "))
    for i in range(numbers):
        list_of_numbers.append(int(input(f"Anna numero {i+1}: ")))    
    return list_of_numbers


def main() -> None:
    """
    Main function to execute the program.
    """
    numbers = ask_for_numbers()
    print(numbers)


if __name__ == "__main__":
    main()