def print_statistics(mean: float, passing_rate:float, grades: dict) -> None:
    """
    Print the statistics of the grades.
    """
    print("Tilasto:")
    print(f"Pisteiden keskiarvo: {mean:.1f}")
    print(f"Hyväksymisprosentti: {passing_rate:.1%}")
    print("Arvosanajakauma:")
    for grade, count in grades.items():
        print(f"  {grade}: {'*' * count}")


def turn_total_points_into_grades(total_points: int) -> int:
    """
    Convert the total points into grades.

    :param total_points: The total points of the student.
    :return: The grade of the student.
    """

    if 15 <= total_points <= 17:
        return 1
    elif 18 <= total_points <= 20:
        return 2
    elif 21 <= total_points <= 23:
        return 3
    elif 24 <= total_points <= 27:
        return 4
    elif 28 <= total_points <= 30:
        return 5
    else:
        return 0


def calculate_grade(total_points_list: list) -> dict:
    """
    Calculate the grade from the list of total points.
    Each student is represented by a tuple of total points and a boolean indicating if they passed.
    """
    grades: dict = {"5": 0, "4": 0, "3": 0, "2": 0, "1": 0, "0": 0}
    for student in total_points_list:
        if student[1] == True:
            grades["0"] += 1
        elif student[1] == False:
            grades[str(turn_total_points_into_grades(student[0]))] += 1
    return grades


def calculate_passing_rate(total_point_list: list) -> float:
    """
    Calculate the passing rate from the list.
    """
    passing_students = 0
    for student in total_point_list:
        if student[1] == False:
            passing_students += 1
    passing_rate = passing_students / len(total_point_list)
    return passing_rate


def calculate_mean_of_total_points(total_point_list: list) -> float:
    """
    Calculate the mean of the total points.
    """
    sum_of_points = 0
    for student in total_point_list:
        sum_of_points += student[0]
    mean = sum_of_points / len(total_point_list)
    return mean


def turn_exercises_into_points(exercises: int) -> int:
    """
    Convert the number of exercises into points.
    """
    if exercises < 10:
        return 0
    elif 10 <= exercises < 20:
        return 1
    elif 20 <= exercises < 30:
        return 2
    elif 30 <= exercises < 40:
        return 3
    elif 40 <= exercises < 50:
        return 4
    elif 50 <= exercises < 60:
        return 5
    elif 60 <= exercises < 70:
        return 6
    elif 70 <= exercises < 80:
        return 7
    elif 80 <= exercises < 90:
        return 8
    elif 90 <= exercises < 100:
        return 9
    elif exercises == 100:
        return 10
    else:
        return 0    
        

def calculate_overall_points(point_list: list) -> list[list[int|bool]]:
    """
    Calculate the overall points from the list of tuples.
    Each tuple contains exam points and exercise points.
    """
    total_points_list = []
    for exam_points, exercises in point_list:
        total_points = exam_points + turn_exercises_into_points(exercises)
        fail = False
        if exam_points < 10:
            fail = True
        if total_points <= 14:
            fail = True 
        total_points_list.append([total_points, fail])
    return total_points_list


def user_prompt() -> list[tuple[int, int]]:
    """
    Prompt the user for a two numbers separated by space.
    These numbers represent the exam and exercise points. 
    """
    point_list = []
    while True:
        user_input: str = input("Koepisteet ja harjoitusten määrä: ")
        if user_input:
            try:
                exam_points_str, exercises_str = user_input.split()
                exam_points = int(exam_points_str)
                exercises = int(exercises_str)
                if not (0 <= exam_points <= 20):
                    raise ValueError("Koepisteet eivät ole välillä 0-20.")
                if not (0 <= exercises <= 100):
                    raise ValueError("Harjoitusten määrä ei ole välillä 0-100.")
                point_list.append((exam_points, exercises))
            except ValueError:
                print("Virheellinen syöte. Yritä uudelleen.")
                continue
        else:
            break
    return point_list

def main() -> None:
    """
    Main function to execute the program.
    """
    point_list = user_prompt()
    total_points_list = calculate_overall_points(point_list)
    mean_of_total_points = calculate_mean_of_total_points(total_points_list)
    passing_rate = calculate_passing_rate(total_points_list)
    grades = calculate_grade(total_points_list)
    print_statistics(mean_of_total_points, passing_rate, grades)


if __name__ == "__main__":
    main()
    