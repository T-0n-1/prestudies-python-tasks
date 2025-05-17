def sum_lists(list1, list2):
    """
    This function takes two lists of numbers and returns a new list that contains the sum of the corresponding elements from both lists.
    
    :param list1: First list of numbers
    :param list2: Second list of numbers
    :return: A new list containing the sum of the corresponding elements from both lists
    """
    # Check if both lists are of the same length
    if len(list1) == len(list2):
        return [x + y for x, y in zip(list1, list2)]
    

def main():
    """
    Main function to execute the program.
    """
    list1 = [1, 2, 3]
    list2 = [7, 8, 9]
    print(f"{sum_lists(list1, list2)}")


if __name__ == "__main__":
    main()