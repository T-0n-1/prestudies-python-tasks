from pathlib import Path
import json


def print_student_info(student_data: str) -> None:
    """
    Print the information of a student.
    :param student: JSON string containing student information.
    """
    students = json.loads(student_data)
    for student in students:
        print(f"{student['nimi']} ", end = "")
        print(f"{student['ika']} vuotta (", end = "")
        for harrastus in student['harrastukset']:
            if harrastus != student['harrastukset'][-1]:
                print(f"{harrastus}", end = ", ")
            else:
                print(f"{harrastus}", end = "")
        print(")")
            
    
def read_json_file(path: Path) -> str:
    """
    Read a JSON file and return its content as a list.
    :param path: Path to the JSON file.
    :return: List of dictionaries containing the JSON data.
    """
    with path.open("r") as file:
        data = file.read()
    return data


def define_path() -> Path:
    """
    Define the path to the JSON file.
    :return: Path object pointing to the JSON file.
    """
    # return Path(input("Enter the path to the JSON file: "))
    return Path("tietoa_opiskelijoista.json")


def main() -> None:
    """
    Main function to handle the JSON file.
    """
    path = define_path()
    students = read_json_file(path)
    print_student_info(students)
    

if __name__ == "__main__":
    main()