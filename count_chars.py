def highest_count(dictionary: dict) -> str:
    """
    Find the character with the highest count in a dictionary.
    
    Args:
        dictionary (dict): A dictionary with characters as keys and their counts as values.
        
    Returns:
        str: The character with the highest count.
    """
    return max(dictionary, key=dictionary.get)


def count_chars(string: str) -> dict:
    """
    Count the occurrences of each character in a string.
    
    Args:
        string (str): The string to count characters from.
        
    Returns:
        dict: A dictionary with characters as keys and their counts as values.
    """
    char_count: dict = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


def main() -> None:
    """
    Main function to execute the program.
    """
    jono1 = "abcbdbe"
    jono2 = "esimerkkimerkkijonokki"

    print(f"Jono 1: {jono1} ja eniten on kirjainta {highest_count(count_chars(jono1))}")
    print(f"Jono 2: {jono2} ja eniten on kirjainta {highest_count(count_chars(jono2))}")


if __name__ == "__main__":
    main()