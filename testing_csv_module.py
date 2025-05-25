from pathlib import Path
import csv


def write_csv_file(file_path: Path, data: dict[str, int]) -> None:
    """
    Write a dictionary to a CSV file.
    :param file_path: Path to the CSV file.
    :param data: Dictionary containing names and ages.
    """
    with file_path.open("w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Age"])
        for name, age in data.items():
            writer.writerow([name, age])


def prompt_for_csv_file() -> Path:
    """
    Prompt the user to enter a CSV file path.
    Returns a Path object representing the file.
    :return: Path to the CSV file.
    """
    file_path = Path(input("Enter the path to the CSV file: "))
    if file_path.suffix.lower() != '.csv':
        file_path = file_path.with_suffix('.csv')    
    return file_path


def prompt_for_age(list_of_names: list[str]) -> dict[str, int]:
    """
    Prompt the user to enter ages for each name in the provided list.
    Returns a dictionary mapping names to their ages.
    :param list_of_names: List of names to prompt for ages.
    :return: Dictionary mapping names to ages.
    """
    children_dict = {}
    for name in list_of_names:
        age = input (f"Enter the age of {name}: ")
        children_dict[name] = int(age) if age.isdigit() else 0
    return children_dict


def prompt_for_children_names() -> list[str]:
    """
    Prompt the user to enter names of children, separated by commas.
    Returns a list of names.
    """
    names_list = []
    while True:
        names = input("Enter the name of the child (empty for exit): ")
        if names.strip() == "":
            break
        names_list.append(names.strip())
    return names_list


def main() -> None:
    """
    Main function to execute the CSV writing process.
    Prompts for names, ages, and file path, then writes to the CSV file.
    """
    names_list = prompt_for_children_names()
    children_dict = prompt_for_age(names_list)
    print(children_dict)
    csv_file_path = prompt_for_csv_file()
    write_csv_file(csv_file_path, children_dict)
    print(f"Data written to {csv_file_path}")


if __name__ == "__main__":
    main()