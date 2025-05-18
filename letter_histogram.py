def letter_histogram(string: str) -> None:
    """
    Returns a dictionary with the count of each letter in the input string.
    
    :param string: The input string to analyze.
    :return: A dictionary with letters as keys and their counts as values.
    """
    histogram = {}
    for char in string:
        if not char in histogram:
            histogram[char] = 1
        else:
            histogram[char] += 1
    for char, count in histogram.items():
        print(f"{char} {'*' * count}")


letter_histogram("abba")