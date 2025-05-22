"""
In this file, there are several functions with related purposes. The functions
each have both a documentation string in them, and also contain a bug in the
code. The bugs are of of different complexity. Your task is to identify the
bugs and fix them.

Rules:
1. The function documentation strings should not be changed, as they are
correct in describing what the function is supposed to do. Instead, you should
fix the code to make the function work as described in the documentation string.

2. You should not change the function names, as they are used in the tests.

3. You should not change the number of arguments the functions take, as they
are also required for tests.

Grading of this assignment is based on the number of bugs you find and fix.
There is at least one bug in each function, but there may be more. The bugs
can be of different types.

It can be helpful to try and call the functions from the python console to see
what they return, and to try and understand what the bug might be.
"""


def sum_of_squares(number1:  int, number2: int) -> int:
    """
    Returns the sum of the squares of two numbers. The square of a number is
    the number multiplied by itself, or the number raised to the power of 2.

    Parameters:
    number1 (int): The first number
    number2 (int): The second number

    Returns:
    int: The sum of the squares of the two numbers

    Example:
    >>> sum_of_squares(2, 4)
    20
    """
    square1: int = number1 ** 2
    square2: int = number2 ** 2
    sum_of_squares: int = square1 + square2
    return sum_of_squares


def caps_lock(input_string: str) -> str:
    """
    Returns an input string and changes all letters to uppercase letters. The
    function should not change any special characters, but rather leave them as
    they are.

    Parameters:
    input_string (str): The input string

    Returns:
    str: The input string with all letters changed to uppercase letters

    Example:
    >>> caps_lock("hello, world!")
    'HELLO, WORLD!'
    """
    # Create an empty string to store the uppercase letters in
    block_letter_string: str = ''

    # Iterate through the input string and add all letters to the output string
    for char in input_string:
        # Use the .isalpha method to check if the character is a letter
        if char.isalpha():
            # Use the .upper method to return the uppercase version of the letter
            block_letter_string += char.upper()

        else:
            block_letter_string += char

    return block_letter_string


def rock_paper_scissors_helper(opposition_choice: str) -> str:
    """
    Tells the user which option to choose in a game of rock-paper-scissors.
    If the opposition choice input is not in 'rock', 'paper', or 'scissors',
    the function will return 'Invalid choice'.

    In a game of rock-paper-scissors, rock beats scissors, scissors beats
    paper, and paper beats rock. This function will return the choice the user
    should make to win against the opposition.

    Parameters:
    opposition_choice (str): The choice of the opposition

    Returns:
    str: The choice the user should make to win

    Example:
    >>> rock_paper_scissors_helper('rock')
    'paper'
    """
    # Check the opposition's choice and return the choice that beats it
    if opposition_choice == 'rock':
        return 'paper'
    elif opposition_choice == 'paper':
        return 'scissors'
    elif opposition_choice == 'scissors':
        return 'rock'
    else:
        return 'Invalid choice'


def save_list_of_strings_as_txt(list: list, filename: str) -> None:
    """
    Saves a list of strings to a text file. Each string in the list should be
    on a new line in the text file.

    Parameters:
    list (list): A list of strings
    filename (str): The name of the file to save the list to

    Returns:
    None

    Example:
    >>> save_list_of_strings_as_txt(['hello', 'world'], 'hello_world.txt')
    """
    # Open the file in write mode
    with open(filename, 'w') as file:
        # Iterate through the list and write each string to the file
        for string in list:
            string += '\n'
            file.write(string)

"""
INTRO TO REQUESTS:
The last function utilises the requests-library. The requests-library is a
library that allows you to send HTTP requests.

HTTP requests (Hyper Text Transfer Protocol) are the way communication over
the internet functions. The requests library in Python allows us to send HTTP
requests and get responses.

You can try putting the url
'https://api.frankfurter.app/latest?from=GBP&to=USD'
to your browser address bar to see the response. The requests library allows us
to do this in Python, without rendering the page in a browser. You could
simplify this by saying that you can use the internet through a command line
or through code with ease, using simple HTTP requests.

The Frankfurter API is a simple API that returnscurrency exchange rates in the
form of a JSON. A JSON is a data format that is easy to work with in Python.
It is similar to a dictionary, with key-value pairs.

An example of such a JSON response from the currency-exchange API is given below:

>>> import requests
>>> response = requests.get('https://api.frankfurter.app/latest?from=GBP&to=USD')
>>> response.json()
{
  "amount": 1,
  "base": "GBP",
  "date": "2024-06-10",
  "rates": {
    "USD": 1.2719
  }
}
"""


def price_calculator(price: float, base_currency: str, target_currency: str) -> float:
    """
    Get the exchange rate between two currencies.

    Parameters:
    price (float): The price to convert
    base_currency (str): The currency to convert from
    target_currency (str): The currency to convert to

    Returns:
    float: The price after the currency exchange

    Example:
    >>> get_price_after_currency_exchange(10, 'GBP', 'USD')
    12.719
    """
    import requests

    currency_url = 'https://api.frankfurter.app'

    # Get a random fact
    response = requests.get(f'{currency_url}/latest',
                            params={'from': base_currency, 'to': target_currency})
    
    exchange_rate = response.json()['rates'][target_currency]

    return price * exchange_rate