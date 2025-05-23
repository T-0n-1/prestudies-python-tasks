from string import ascii_lowercase, digits
from random import randint


def password_charpool(selection: str) -> str:
    """
    Generate a character pool for password generation.
    The pool might contain lowercase letters, digits and special characters !?=+-()#.
    :param selection: Selection of characters to include in the pool.
                      'l' for lowercase letters, 'd' for digits, 's' for special characters.
    :return: String containing the selected characters.
    """
    pool = ""
    if 'l' in selection:
        pool += ascii_lowercase
    if 'd' in selection:
        pool += digits
    if 's' in selection:
        pool += "!?=+-()#"
    return pool
    


def generate_password(length: int, digits: bool, special: bool) -> str:
    """
    Generate a random password of a given length.
    The password will contain lowercase letters.
    :param length: Length of the password to be generated.
    :param digits: Include digits in the password.
    :param special: Include special characters in the password.
    :return: Randomly generated password.
    """
    password = ""
    password_pool_selection = "l"
    if digits:
        password_pool_selection += "d"
    if special:
        password_pool_selection += "s"
    password_pool = password_charpool(password_pool_selection)
    for _ in range(length):
        # Generate a random index to select a character from ascii_lowercase
        index = randint(0, len(password_pool) - 1)
        password += password_pool[index]
    return password


def main():
    """
    Main function to demonstrate password generation.
    """
    for i in range(10):
        print(generate_password(12, True, True))
    print()    
    print(generate_password(12, True, False))
    print()    
    print(generate_password(12, False, True))


if __name__ == "__main__":
    main()