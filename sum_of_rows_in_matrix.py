def redefine_matrix(matrix: list[list[int]]) -> None:
    """
    Redefines a matrix by summing each row and appending the sum to row.
    
    :param matrix (list[list[int]]): A 2D list representing the matrix.
        
    Returns:
        None - redefines the matrix given as parameter.
    """
    for row in matrix:
        row.append(sum(row))


def main():
    """
    Main function to demonstrate the redefinition of a matrix.
    """
    matriisi = [[1, 2], [3, 4]]
    redefine_matrix(matriisi)
    print(matriisi)


if __name__ == "__main__":
    main()