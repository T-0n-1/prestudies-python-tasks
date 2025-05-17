def from_negative(num: int) -> None:
    """
    Prints the numbers from the given numbers negative to -1
    """
    for i in range(-num, 0, 1):
        print(i)


def to_positive(num: int) -> None:
    """
    Prints the numbers from 1 to the given number
    """
    for i in range(1, num + 1):
        print(i)


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
            from_negative(luku)
            to_positive(luku)
        else:
            print("Moi!")
            break


if __name__ == "__main__":
    main()