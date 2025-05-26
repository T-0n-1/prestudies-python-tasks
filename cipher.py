"""In this assignment you must implement the Caesar cipher encryption and
decryption algorithms. The Caesar cipher is a substitution cipher where each
letter in the plain text is shifted a certain number of places down the
alphabet. For example, the word "Python" encrypted with Caesar cipher and a
shift length of 2 would result in "Ravjqp" as the letter R is two after P, the
letter a is two after y (next is z and then the alphabet wraps around to a),
the letter v is two after t, and so on.

More information about Caesar cipher can be found here:
https://en.wikipedia.org/wiki/Caesar_cipher

In this exercise, you must complete the encrypt and decrypt methods to
abide by the ciphering rules. The encrypt method should take a text and a
shift number and return the encrypted text. The decrypt method should take
an encrypted text and a shift number and return the decrypted text.

For the purpose of this exercise, consider the following rules:
    1. Leave the function definitions and names as they are.
    2. The functions should not alter any special characters or numbers
    3. The functions should return a string with a return statement
    4. You can consider the English alphabet only, both lower and upper case
    5. The alphabet should "wrap around" so that if you reach the end of
    the alphabet and continue shifting you should go back to the beginning

For a perfect score, try to also abide by the following rules:
    1. The encrypt and decrypt methods should be case sensitive, meaning that
    lower case letters should be encrypted to lower case letters and upper
    case letters to upper case letters
    2. Do not use any external libraries
    3. The encrypt and decrypt methods should be able to handle any shift,
    even larger than 26 or negative numbers, as long as it is an integer

HINTS:
    1. The ord() function returns an integer representing the Unicode number
    of a character

>>> ord('a')
97

    2. The chr() function returns a character representing the Unicode number

>>> chr(97)
'a'

    3. The isalpha() method returns True if all the characters of a string
    are alphabet letters (a-z)

>>> 'abc'.isalpha()
True

    4. You can use the decrypt and encrypt methods to test each other

    5. You can define helpful variables outside the functions to use them

Save the file as cipher.py and keep the function names as they are. Do not
change the function names or the parameters they take. You can add more
functions if you need to, but do not change the names of the existing ones
and make sure that they are the two functions that do the encryption and
decryption.

Some of the examples that will be checked when grading submissions are:

>>> from cipher.py import encrypt, decrypt
>>> encrypt("abc", 2)
'cde'
>>> decrypt("bcd", 1)
'abc'
>>> encrypt("xyz", 2)
'zab'
>>> encrypt("Hello, world!", 5)
'Mjqqt, btwqi!'

You can try these cases against your own functions from the python console to
check your solution before submitting it.

Below are templates for the functions you need to implement.
"""
lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def encrypt(text: str, shift: int) -> str:
    encrypted_text: str = ''
    for char in text:
        alphabet = lower if char.islower() else upper if char.isupper() else None
        if alphabet == None:
            encrypted_text += char
        else:    
            index: int = (alphabet.index(char) + shift) % len(alphabet)
            encrypted_text += alphabet[index]
    return encrypted_text


def decrypt(text: str, shift: int) -> str:
    decrypted_text: str = ''
    for char in text:
        alphabet = lower if char.islower() else upper if char.isupper() else None
        if alphabet == None:
            decrypted_text += char
        else:    
            index: int = (alphabet.index(char) - shift) % len(alphabet)
            decrypted_text += alphabet[index]
    return decrypted_text