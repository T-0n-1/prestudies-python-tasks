def items_in_matrix(matrix: list, item: int) -> int:
    """
    This function counts the number of occurrences of a given item in a 2D matrix.

    :param matrix: A 2D list (list of lists) representing the matrix.
    :param item: The item to count in the matrix.
    :return: The count of occurrences of the item in the matrix.
    """
    count = 0
    for row in matrix:
        count += row.count(item)
    return count

m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]

print(items_in_matrix(m, 1))  