def recalculate_points(point_list: list) -> list:
    """
    Build new points list after defining the exercises into points.
    """
    return [exam_points, exercises = turn_exercises_into_points(exercises) for exam_points, exercises in point_list]


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
    


