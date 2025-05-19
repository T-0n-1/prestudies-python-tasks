def highest(file_name: str) -> int:
    """
    Read a file and return the highest number in it.
    """
    with open(file_name, "r") as file:
        numbers = [int(line.strip()) for line in file]
    return max(numbers)


def main():
    """
    Main function to execute the program.
    """
    highest_number = highest("numbers.txt")
    print(f"The highest number in the file is: {highest_number}")


if __name__ == "__main__":
    main()