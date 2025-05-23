from pathlib import Path


def save_filtered_into_file(lottery_numbers: dict, filepath: Path) -> None:
    """
    Save the filtered lottery numbers into a file.

    :param lottery_numbers: Dictionary containing filtered lottery numbers.
    :param filepath: Path to the file where the filtered numbers will be saved.
    """
    filepath = Path("korjatut_" + filepath.name)
    with filepath.open("a") as file:
        for week, numbers in lottery_numbers.items():
            week_with_numbers = f"{week}: {', '.join(numbers)}\n"
            file.write(week_with_numbers)
    

def filter_lottery_numbers(lottery_numbers: dict) -> dict:
    """
    Filter the correct lottery number rows from possibly incorrect ones.

    :param lottery_numbers: Dictionary containing lottery numbers.
    :return: A dictionary with the filtered lottery numbers.
    """
    filtered_lottery_numbers = {}
    for week, numbers in lottery_numbers.items():
        _, week_number = week.split(" ")
        if (not all(number.isdigit() and 1 <= int(number) <= 39 for number in numbers) or 
            not week_number.isdigit() or int(week_number) < 1 or int(week_number) > 52 or
            len(numbers) != 7 or len(set(numbers)) == 7):
            continue
        else:
            filtered_lottery_numbers[week] = numbers
    return filtered_lottery_numbers


def convert_file_into_dictionary(lottery_numbers: Path) -> dict:
    """
    Filter the lottery number rows from the given file.
    
    :param lottery_numbers: Path to the file containing lottery numbers.
    :return: A dictionary with the filtered lottery numbers.
    """
    lottery_numbers_dict = {}
    for line in lottery_numbers.read_text().splitlines():
        week, numbers = line.split(";")
        number_list = [num.strip() for num in numbers.split(",") if num.strip()]
        lottery_numbers_dict[week.strip()] = number_list
    return lottery_numbers_dict

def define_filepath(filepath: str) -> Path:
    """
    Define the file path for the lottery numbers.
    """
    return Path(filepath)


def main():
    """
    Main function to execute the script.
    """
    filepath = define_filepath("lottonumerot.csv")
    lottery_numbers = convert_file_into_dictionary(filepath)
    filtered_lottery_numbers = filter_lottery_numbers(lottery_numbers)
    save_filtered_into_file(filtered_lottery_numbers, filepath)


if __name__ == "__main__":
    main()