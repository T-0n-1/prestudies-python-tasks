def factorial(number: int) -> dict:
    """
    Calculate the factorial of a number and return a dictionary with the number and its factorial.
    """
    dictionary = {}
    total = 1
    for i in range(1, number + 1):
        total *= i
        dictionary[i] = total
    return dictionary


k = factorial(5)
print(k[1])
print(k[3])
print(k[5])