import json
import urllib.request
import http.client


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


def decode_response(response: http.client.HTTPResponse) -> str:
    """Decode the response from the API to a string.
    :param response: The response object from the API.
    :return: The decoded response as a string.
    """
    return response.read().decode("utf-8")
    

def get_course_stats() -> http.client.HTTPResponse:
    """Fetch course statistics from the API.
    Returns:
        http.client.HTTPResponse: The response object containing course statistics.
    """
    url = "https://studies.cs.helsinki.fi/stats-mock/api/courses"
    response = urllib.request.urlopen(url)
    return response


def get_all() -> None:
    """Main function to fetch and print course statistics."""
    kurssitiedot = get_course_stats()
    kurssitiedot_decoded = decode_response(kurssitiedot)
    kurssitiedot_json = convert_into_json(kurssitiedot_decoded)
    all_enabled = get_all_enabled_courses(kurssitiedot_json)
    print(all_enabled)


def main() -> None:
    """Main entry point of the script."""
    get_all()


if __name__ == "__main__":
    main()