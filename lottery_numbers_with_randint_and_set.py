def remove_duplicates(numbers):
    """
    Remove duplicates from the list of numbers.
    """
    return list(set(numbers))


def generate_lottery_numbers(how_many_numbers: int, min_number: int, max_number: int) -> list:
    """
    Generate a list of 7 unique random lottery numbers between 1 and 49.
    """
    from random import randint

    numbers = []
    while len(numbers) < how_many_numbers:
        number = randint(min_number, max_number)
        numbers.append(number)
        numbers = remove_duplicates(numbers)
    return sorted(numbers)


def main():
    """
    Main function to generate and print lottery numbers.
    """
    lottery_numbers = generate_lottery_numbers(7, 1, 40)
    # print("Your lottery numbers are:", ", ".join(str(num) for num in lottery_numbers))
    for number in lottery_numbers:
        print(number)


if __name__ == "__main__":
    main()