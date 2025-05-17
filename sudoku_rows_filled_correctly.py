def row_right(matrix: list, row: int) -> bool:
    """
    This function checks if a specific row in a 2D matrix, sudoku, is filled correctly.

    :param matrix: A 2D list (list of lists) representing the matrix.
    :param row: The index of the row to check for uniqueness.
    :return: True if all elements in the specified row are unique, False otherwise.
    """
    row_to_check = matrix[row]
    zeroes_removed = [num for num in row_to_check if num != 0]
    unique_elements = list(set(zeroes_removed))
    return len(zeroes_removed) == len(unique_elements)


sudoku = [
  [9, 0, 0, 0, 8, 0, 3, 0, 0],
  [2, 0, 0, 2, 5, 0, 7, 0, 0],
  [0, 2, 0, 3, 0, 0, 0, 0, 4],
  [2, 9, 4, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 7, 3, 0, 5, 6, 0],
  [7, 0, 5, 0, 6, 0, 4, 0, 0],
  [0, 0, 7, 8, 0, 3, 9, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 3],
  [3, 0, 0, 0, 0, 0, 0, 0, 2]
]

print(row_right(sudoku, 0))
print(row_right(sudoku, 1))
