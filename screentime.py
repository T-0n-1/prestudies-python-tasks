from pathlib import Path
from datetime import datetime, timedelta


def build_and_write_file(screentimes: dict, path: Path, starting_day: datetime, end_day: datetime, total_minutes: int, mean: float) -> None:
    """
    Builds a string from the screentimes dictionary and writes it to a file.
    Also appends the total minutes and mean screen time.
    :param screentimes: Dictionary with dates as keys and lists of screen times as values.
    :param path: Path to the file where the data will be written.
    :param end_day: The last day of the screen time logging period.
    :param total_minutes: Total screen time in minutes.
    :param mean: Mean screen time per day.
    """
    with path.open("a") as file:
        file.write(f"Ajanjakso {starting_day.strftime("%d.%m.%Y")}-{end_day.strftime("%d.%m.%Y")}\n")
    with path.open("a") as file:
        file.write(f"Yht. minuutteja: {total_minutes}\n")
    with path.open("a") as file:
        file.write(f"Keskim. minuutteja: {mean:.1f}\n")
    day = starting_day
    while day != end_day + timedelta(days=1):
        pvm = day.strftime("%d.%m.%Y")
        if pvm in screentimes:
            times = screentimes[pvm]
            with path.open("a") as file:
                file.write(f"{pvm}: {times[0]}/{times[1]}/{times[2]}\n")
        day += timedelta(days=1)
    


def total_minutes(screentimes: dict) -> int:
    """
    Calculates the total screen time in minutes from the screentimes dictionary.
    :param screentimes: Dictionary with dates as keys and lists of screen times as values.
    :return: Total screen time in minutes.
    """
    total = 0
    for _, times in screentimes.items():
        for time in times:
            total += int(time)
    return total
            

def prompt_for_screen_time(starting_day: datetime, end_day: datetime) -> dict:
    """
    Prompts the user for screen time for each day in the specified range and writes it to a file.
    """
    screentimes: dict = {}
    day = starting_day
    print("Anna ruutuajat kunakin päivänä minuutteina (TV tietokone mobiili)")
    while day != end_day + timedelta(days=1):
        pvm = day.strftime("%d.%m.%Y")
        tv, tietokone, mobiili = input(f"Ruutuaika {pvm}: ").split(" ")
        screentimes[pvm] = [tv, tietokone, mobiili]
        day += timedelta(days=1)
    return screentimes


def prompt_user() -> tuple[Path, datetime, int]:
    """
    Prompts the user for the name of file without the suffix and starting day with duration 
    and returns them as a tuple.
    """
    path: Path = Path(input("Tiedosto: "))
    if path.suffix != ".txt":
        path = path.with_suffix(".txt")
    try:
        starting_day = datetime.strptime(input("Aloituspäivä: "), "%d.%m.%Y")
    except ValueError:
        print("Virheellinen päivämäärämuoto. Käytä muotoa dd.mm.yyyy.")
        return prompt_user()
    try:
        duration = int(input("Montako päivää: "))
    except ValueError:
        print("Virheellinen kesto. Anna kokonaisluku.")
        return prompt_user()
    return path, starting_day, duration


def main() -> None:
    """
    Main function to execute the screen time logging.
    """
    path, starting_day, duration = prompt_user()
    end_day = starting_day + timedelta(days=duration - 1)
    screentimes = prompt_for_screen_time(starting_day, end_day)
    minutes_in_total = total_minutes(screentimes)
    mean = minutes_in_total / duration
    build_and_write_file(screentimes, path, starting_day, end_day, minutes_in_total, mean)


if __name__ == "__main__":
    main()