def combine_data(students: dict, tasks: dict) -> None:
    """
    Combine student and task data and print the results.
    """
    for student_id, student_data in students.items():
        task_sum = 0
        for task_grade in tasks[student_id]:
            task_sum += int(task_grade)
        print(f"{student_data[0]} {student_data[1]} {task_sum}") 


def read_file(file_path: str) -> dict:
    """
    Read a CSV file and return its contents as a dictionary.
    """
    data = {}
    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            opnro, *rest = line.split(";")
            if opnro == "opnro":
                continue
            data[opnro] = rest
    return data 


def user_prompt() -> tuple:
    """
    Prompt the user for two names of files and return them as a tuple.
    """
    # student_information = input("Opiskelijatiedot: ")
    # task_information = input("Tehtävätiedot: ")
    # return student_information, task_information
    return "opiskelijat.csv", "tehtavat.csv"


def main() -> None:
    """
    Main function to execute the program.
    """
    student_file, task_file = user_prompt()
    students = read_file(student_file)
    tasks = read_file(task_file)
    combine_data(students, tasks)

if __name__ == "__main__":
    main()
    