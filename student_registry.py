def student_statistics(students: dict) -> None:
    """
    Compiles a list of students and their courses.
    
    :param students: List of students
    """
    if students:
        stats = []
        for student in students:
            course_list = get_student_courses(students, student)
            if course_list:
                mean_of_courses = sum(grade for _, grade in course_list) / len(course_list)
                stats.append((student, len(course_list), mean_of_courses))
        print(f"opiskelijoita {len(students)}")
        print(f"eniten suorituksia {max(stats, key=lambda x: x[1])[1]} {max(stats, key=lambda x: x[1])[0]}")
        print(f"paras keskiarvo {max(stats, key=lambda x: x[2])[2]:.1f} {max(stats, key=lambda x: x[2])[0]}")
                
    
def add_course(students: dict, student: str, new_course: tuple[str, int]) -> None:
    """
    Adds a course and grade for a student.
    
    :param students: List of students
    :param student: Student to whom the course is added
    :param new_course: Course to be added
    :param grade: Grade for the course
    """
    if student in students:
        course, grade = new_course
        if not grade <= 0:
            if course in students[student]:
                if not students[student][course] >= grade:
                    students[student][course] = grade        
            else: 
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


def main() -> None:
    opiskelijat: dict = {}
    print("-" * 35)
    add_student(opiskelijat, "Pekka")
    add_student(opiskelijat, "Liisa")
    print_student(opiskelijat, "Pekka")
    print_student(opiskelijat, "Liisa")
    print_student(opiskelijat, "Jukka")
    print("-" * 35)
    add_course(opiskelijat, "Pekka", ("Ohpe", 3))
    add_course(opiskelijat, "Pekka", ("Tira", 2))
    print_student(opiskelijat, "Pekka")
    print("-" * 35)
    add_course(opiskelijat, "Pekka", ("Ohpe", 3))
    add_course(opiskelijat, "Pekka", ("Tira", 2))
    add_course(opiskelijat, "Pekka", ("Lama", 0))
    add_course(opiskelijat, "Pekka", ("Ohpe", 2))
    print_student(opiskelijat, "Pekka")
    print("-" * 35)
    add_course(opiskelijat, "Pekka", ("Lama", 1))
    add_course(opiskelijat, "Liisa", ("Ohpe", 5))
    add_course(opiskelijat, "Liisa", ("Jtkt", 4))
    student_statistics(opiskelijat)
    print("-" * 35)


if __name__ == "__main__":
    main()