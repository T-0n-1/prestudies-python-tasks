def add_item(sudoku: list, row: int, column: int, value: int) -> None:
    """
    Add a value to the sudoku grid at the specified row and column.
    
    :param sudoku: The sudoku grid (2D list)
    :param row: The row index (0-8)
    :param column: The column index (0-8)
    :param value: The value to add (1-9)
    """
    if 0 <= row < 9 and 0 <= column < 9 and 1 <= value <= 9:
        sudoku[row][column] = value
    else:
        raise ValueError("Invalid row, column, or value")
    

def print_sudoku(sudoku: list) -> None:
    """
    Print the sudoku grid in a formatted way.

    :param sudoku: The sudoku grid (2D list)
    """
    for row_index, row in enumerate(sudoku):
        if row_index == 3 or row_index == 6:
            print()
        for column_index, value in enumerate(row):
            to_print = "_" if value == 0 else value
            if column_index == 3 or column_index == 6:
                print(" ", end="")
            print(to_print, end=" ")
        print()


sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]
print_sudoku(sudoku)
add_item(sudoku, 0, 0, 2)
add_item(sudoku, 1, 2, 7)
add_item(sudoku, 5, 7, 3)
print()
print("Kolme numeroa lisätty:")
print()
print_sudoku(sudoku)