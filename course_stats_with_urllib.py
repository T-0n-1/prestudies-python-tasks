import json
from math import floor
from urllib.request import urlopen
from http.client import HTTPResponse


def build_unique_course_stats(course_stats_list: list) -> dict:
    """Build a dictionary of unique course statistics from a list of course stats.
    :param course_stats_list: A list of dictionaries containing course statistics.
    :return: A dictionary with course statistics. 
    """
    dictionary = {}
    weeks_total = len(course_stats_list)
    students_list = []
    total_hours_list = []
    total_exercises_list = []
    for week in course_stats_list:
        for key in course_stats_list[week]:
            if key == "students":
                students_list.append(course_stats_list[week][key])
            elif key == "hour_total":
                total_hours_list.append(course_stats_list[week][key])
            elif key == "exercise_total":
                total_exercises_list.append(course_stats_list[week][key])            
    max_of_students = max(students_list) if students_list else 0
    total_of_hours_total = sum(total_hours_list) if total_hours_list else 0
    average_of_hours = floor(total_of_hours_total / max_of_students) if max_of_students > 0 else 0
    total_of_exercises = sum(total_exercises_list) if total_exercises_list else 0
    average_of_exercises = floor(total_of_exercises / max_of_students) if max_of_students > 0 else 0
    dictionary["viikkoja"] = weeks_total
    dictionary["opiskelijoita"] = max_of_students
    dictionary["tunteja"] = total_of_hours_total
    dictionary["tunteja_keskimaarin"] = average_of_hours
    dictionary["tehtavia"] = total_of_exercises
    dictionary["tehtavia_keskimaarin"] = average_of_exercises
    return dictionary


def get_unique_course_stats(name: str) -> dict:
    """Get a unique course by its name.
    :param name: The name of the course to search for.
    :return: A dictionary containing the course details if found, otherwise an empty dictionary.
    """
    url = f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{name}/stats"
    course_stats_decoded = decode_response(urlopen(url))
    return build_unique_course_stats(convert_into_json(course_stats_decoded))
    

def get_all_enabled_courses(courses: list) -> list[tuple]:
    """Get all enabled courses from the provided list of courses.
    :param courses: A list of course dictionaries.
    :return: A list of tuples containing course name, ID, year and sum of exercises for enabled courses.
    """
    return [
        (
            course["fullName"],
            course["name"],
            course["year"],
            sum(exercise for exercise in course["exercises"]),
        )
        for course in courses
        if course["enabled"]
    ]
    

def convert_into_json(string: str) -> list:
    """Convert a JSON string into a Python list.
    :param string: The JSON string to convert.
    :return: A list representation of the JSON string.
    """
    return json.loads(string)


def decode_response(response: HTTPResponse) -> str:
    """Decode the response from the API to a string.
    :param response: The response object from the API.
    :return: The decoded response as a string.
    """
    return response.read().decode("utf-8")
    

def get_course_stats() -> HTTPResponse:
    """Fetch course statistics from the API.
    Returns:
        HTTPResponse: The response object containing course statistics.
    """
    url = "https://studies.cs.helsinki.fi/stats-mock/api/courses"
    response = urlopen(url)
    return response


def get_all() -> list[tuple]:
    """Main function to fetch and print course statistics.
    :return: A list of tuples containing course name, ID, year and sum of exercises for enabled courses.
    """
    course_stats = get_course_stats()
    course_stats_decoded = decode_response(course_stats)
    course_stats_json = convert_into_json(course_stats_decoded)
    return get_all_enabled_courses(course_stats_json)


def main() -> None:
    """Main entry point of the script."""
    print(get_all())
    print()
    for item in get_all():
        print(get_unique_course_stats(item[1]))


if __name__ == "__main__":
    main()