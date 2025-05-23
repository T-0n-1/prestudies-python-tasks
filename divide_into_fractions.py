from fractions import Fraction


def divide_into_fractions(denominator: int) -> list:
    """
    Divide the number 1 into fractions with the given denominator.

    Args:
        denominator (int): The denominator of the fractions.

    Returns:
        list: A list of Fraction objects representing the fractions.
    """
    if denominator < 0:
        raise ValueError("Denominator must be a positive integer.")
    elif denominator == 0:
        raise ZeroDivisionError("Denominator cannot be zero.")
    return [Fraction(1, denominator) for _ in range(denominator)]


def main():
    """
    Main function to test the divide_into_fractions function.
    """
    for p in divide_into_fractions(3):
        print(p)
    print()
    print(divide_into_fractions(5))


if __name__ == "__main__":
    main()