def highest_value(matrix):
    """
    This function takes a matrix as input and returns the highest value in the matrix.
    """
    max_value = 0
    for row in matrix:
        for value in row:
            if value > max_value:
                max_value = value
    return max_value    


def sum_of_all_elements(matrix):
    """
    This function takes a matrix as input and returns the sum of all its elements.
    """
    total_sum = 0
    for row in matrix:
        total_sum += sum(row)
    return total_sum


def read_matrix_from_file(file_path):
    """
    This function reads a matrix from a file with each row on a new line.
    """
    matrix = []
    with open(file_path, "r", encoding="utf-16") as file:
        for line in file:
            line = line.strip()
            values = line.split(",")
            row = []
            for value in values:
                row.append(int(value))
            matrix.append(row)
    return matrix


def main():
    matrix = read_matrix_from_file('matriisi.txt')
    sum = sum_of_all_elements(matrix)
    max_value = highest_value(matrix)
    print(f"The sum of all elements in the matrix is: {sum}")
    print(f"The highest value in the matrix is: {max_value}")


if __name__ == "__main__":
    main()