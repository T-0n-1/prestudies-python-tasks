



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


def user_prompt() -> None:
    """
    Prompt the user for a two numbers separated by space.
    These numbers represent the exam and exercise points. 
    """
    point_list = []
    while True:
        user_input = input("Koepisteet ja harjoitusten määrä: ")
        if user_input:
            try:
                exam_points, exercises = user_input.split()
                exam_points = int(exam_points)
                if not (0 <= exam_points <= 20):
                    raise ValueError("Koepisteet eivät ole välillä 0-20.")
                exercises = int(exercises)
                if not (0 <= exercises <= 100):
                    raise ValueError("Harjoitusten määrä ei ole välillä 0-100.")
                point_list.append(tuple(exam_points, exercises))
            except ValueError:
                print("Virheellinen syöte. Yritä uudelleen.")
                continue
        else:
            break
    return point_list
    


