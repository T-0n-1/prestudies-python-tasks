def is_palindrome(word: str) -> bool:
    """
    Check if a word is a palindrome.
    
    A palindrome is a word that reads the same backward as forward.
    
    Args:
        word (str): The word to check.
        
    Returns:
        bool: True if the word is a palindrome, False otherwise.
    """
    return word.lower() == "".join(reversed(word.lower()))

def prompt_for_word() -> str:
    """
    Ask the user for a word.
    
    Returns:
        str: The word entered by the user.
    """
    return input("Anna palindromi: ")


def main() -> None:
    """
    Main function to execute the program.
    """
    while True:
        sana = prompt_for_word()
        if is_palindrome(sana):
            print(f"{sana} on palindromi!")
        else:
            print("ei ollut palindromi")


if __name__ == "__main__":
    main()