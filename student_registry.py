def add_course(students: dict, student: str, course: tuple[str, int]) -> None:
    """
    Adds a course and grade for a student.
    
    :param students: List of students
    :param student: Student to whom the course is added
    :param course: Course to be added
    :param grade: Grade for the course
    """
    if student in students:
        course, grade = course
        students[student][course] = grade
    else:
        print(f"ei löytynyt ketään nimellä {student}")


def get_student_courses(students: dict, student: str) -> list:
    """
    Returns the courses of a student.
    
    :param students: List of students
    :param student: Student whose courses are to be returned
    :return: List of courses for the student
    """
    course_list: list[tuple[str, int]] = []
    if student in students:
        for course, grade in students[student].items():
            course_list.append((course, grade))
        return course_list
    else:
        return []


def print_student(students: dict, student: str) -> None:
    """
    Prints the student from the list of students.
    
    :param students: List of students
    :param student: Student to be printed
    """
    if student in students:
        course_list = get_student_courses(students, student)
        print(f"{student}: ")
        if course_list:
            print(f" suorituksia {len(course_list)} kurssilta")
            for course, grade in course_list:
                print(f"  {course} {grade}")
            mean_of_courses = sum(grade for _, grade in course_list) / len(course_list)
            print(f" keskiarvo {mean_of_courses:.1f}")
            
        else:
            print(" Ei suorituksia")
    else:
        print(f"ei löytynyt ketään nimellä {student}")


def add_student(students: dict, student: str) -> None:
    """
    Adds a student to the list of students.
    
    :param students: List of students
    :param student: Student to be added
    """
    students[student] = {}