def read_fruits() -> dict:
    """
    Read a file and return a list of fruits.
    
    :param file_name: The name of the file to read.
    :return: A list of fruits.
    """
    fruit_dictionary: dict[str, float] = {}
    with open("hedelmat.csv", "r", encoding="utf-16") as file:
        for line in file:
            fruit, price = line.strip().split(";")
            float_price = float(price)
            fruit_dictionary[fruit] = float_price
    return fruit_dictionary


def main():
    """
    Main function to execute the program.
    """
    fruits = read_fruits()
    print(f"The fruits in the file are: {fruits}")


if __name__ == "__main__":
    main()