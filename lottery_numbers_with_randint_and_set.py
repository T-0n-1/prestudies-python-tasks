def remove_duplicates(numbers):
    """
    Remove duplicates from the list of numbers.
    """
    return list(set(numbers))


def generate_lottery_numbers():
    """
    Generate a list of 7 unique random lottery numbers between 1 and 49.
    """
    from random import randint

    numbers = []
    while len(numbers) < 7:
        number = randint(1, 40)
        numbers.append(number)
        numbers = remove_duplicates(numbers)
    return numbers


def main():
    """
    Main function to generate and print lottery numbers.
    """
    lottery_numbers = generate_lottery_numbers()
    print("Your lottery numbers are:", ", ".join(str(num) for num in lottery_numbers))


if __name__ == "__main__":
    main()