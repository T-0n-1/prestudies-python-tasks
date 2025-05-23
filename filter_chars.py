from string import ascii_letters, punctuation


def filter_chars(input_string: str) -> tuple[str, str, str]:
    """
    Filters chars in string into ascii_letters string, punctuantion string and rest string.

    Args:
        input_string (str): The string to filter.

    Returns:
        tuple: A tuole containing ascii_letter_string, punctuation_string and rest of the chars string.
    """
    ascii = ""
    punct = ""
    rest = ""
    for char in input_string:
        if char in ascii_letters:
            ascii += char
        elif char in punctuation:
            punct += char
        else:
            rest += char
    return ascii, punct, rest


def main():
    input_string = filter_chars("Tämä on testi!!! Toimiiko, mitä?")
    for string in input_string:
        print(string)


if __name__ == "__main__":
    main()