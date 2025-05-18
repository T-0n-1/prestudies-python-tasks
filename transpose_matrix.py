def transpose(matrix: list[list[int]]) -> list[list[int]]:
    """
    Transpose a given matrix.

    Args:
        matrix (list[list[int]]): The matrix to transpose.

    Returns:
        list[list[int]]: The transposed matrix.
    """
    return [list(row) for row in zip(*matrix)]


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
transposed_matrix = transpose(matrix)
print("Original matrix:")
for row in matrix:
    print(row)
print("\nTransposed matrix:")
for row in transposed_matrix:
    print(row)