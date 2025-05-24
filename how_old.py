from datetime import datetime, timedelta


def calculate_the_difference(birthday: datetime) -> timedelta:
    """
    Calculate the difference between the last day of the millennium and the user's birthday.
    
    :param birthday: The user's birthday as a datetime object.
    :return: A timedelta object representing the difference.
    """
    last_day_of_millenium = datetime(1999, 12, 31)
    return last_day_of_millenium - birthday


def prompt_for_birthday() -> tuple[str, str, str]:
    """
    Prompt the user for their birthday and return it as a tuple of (year, month, day).
    """
    day = input("Päivä: ")
    month = input("Kuukausi: ")
    year = input("Vuosi: ")
    return day, month, year


def main() -> None:
    """
    Main function to calculate and print the user's age based on their birthday.
    """
    birthday = datetime.strptime(", ".join(prompt_for_birthday()), "%d, %m, %Y")
    difference = calculate_the_difference(birthday)
    if difference.days < 0:
        print("Et ollut syntynyt, kun vuosituhat vaihtui.")
    else:
        print(f"Olet {difference.days} päivää vanha, kun vuosituhat vaihtui.")


if __name__ == "__main__":
    main()