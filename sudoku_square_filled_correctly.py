def square_right(matrix: list, row: int, column: int) -> bool:
    """
    This function checks if a specific column in a 2D matrix, sudoku, is filled correctly.

    :param matrix: A 2D list (list of lists) representing the matrix.
    :param column: The index of the column to check for uniqueness.
    :return: True if all elements in the specified row are unique, False otherwise.
    """
    square_to_check = []
    for x in range(row, row + 3):
        for y in range(column, column + 3):
            square_to_check.append(matrix[x][y])
        square_to_check.append(matrix[row][column])     
    zeroes_removed = [num for num in square_to_check if num != 0]
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

print(square_right(sudoku, 0, 0))
print(square_right(sudoku, 1, 2))