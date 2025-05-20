def convert_total_points_to_grade(total_points: int) -> int:
    """
    Convert total points to a grade.
    """
    if 0 <= total_points < 15:
        return 0
    elif 15 <= total_points < 18:
        return 1
    elif 18 <= total_points < 21:
        return 2
    elif 21 <= total_points < 24:
        return 3
    elif 24 <= total_points < 28:
        return 4
    elif total_points >= 28:
        return 5
    else:
        return -1


def task_sum_to_points(task_sum: int) -> int:
    """
    Convert task sum to points.
    """
    helper_for_calc = round(task_sum / 40 * 100, 0)
    if 10 <= helper_for_calc < 20:
        return 1
    elif 20 <= helper_for_calc < 30:
        return 2
    elif 30 <= helper_for_calc < 40:
        return 3
    elif 40 <= helper_for_calc < 50:
        return 4
    elif 50 <= helper_for_calc < 60:
        return 5
    elif 60 <= helper_for_calc < 70:
        return 6
    elif 70 <= helper_for_calc < 80:
        return 7
    elif 80 <= helper_for_calc < 90:
        return 8
    elif 90 <= helper_for_calc < 100:
        return 9
    elif helper_for_calc == 100:
        return 10
    else:
        return 0
    

def print_stats(data: dict) -> None:
    """
    Print the statistics of students, tasks, and exams.
    """
    print(f"{'nimi':30}{'teht_lkm':10}{'teht_pist':10}{'koe_pist':10}{'yht_pisteet':10}{'arvosana':10}")
    for student, grades in data.items():
        task_sum = grades[0]
        exam_sum = grades[1]
        task_points = task_sum_to_points(task_sum)
        total_points = task_points + exam_sum
        grade = convert_total_points_to_grade(total_points)
        print(f"{student:30}{task_sum:<10}{task_points:<10}{exam_sum:<10}{total_points:<10}{grade:<10}")
        

def combine_data(students: dict, tasks: dict, exams: dict) -> dict:
    """
    Combine student and task data and print the results.
    """
    data = {}
    for student_id, student_data in students.items():
        task_sum = 0
        for task_grade in tasks[student_id]:
            task_sum += int(task_grade)
        exam_sum = 0
        for exam_grade in exams[student_id]:
            exam_sum += int(exam_grade)
        student_name = student_data[0] + " " + student_data[1]
        data[student_name] = [task_sum, exam_sum]
    return data 


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
    # exam_information = input("Koepisteet: ")
    # return student_information, task_information, exam_information
    return "opiskelijat.csv", "tehtavat.csv", "koepisteet.csv"


def main() -> None:
    """
    Main function to execute the program.
    """
    student_file, task_file, exam_file = user_prompt()
    students, tasks, exams = [read_file(argument) for argument in [student_file, task_file, exam_file]]
    student_statistics = combine_data(students, tasks, exams)
    print_stats(student_statistics)


if __name__ == "__main__":
    main()
    