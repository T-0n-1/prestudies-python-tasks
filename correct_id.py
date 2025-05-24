from datetime import datetime


def valitade_checksum(id: str) -> bool:
    """
    Validates if the given ID has a valid checksum.
    
    Args:
        id (str): The ID to validate.
        
    Returns:
        bool: True if the ID is valid, False otherwise.
    """
    check_char_string = "0123456789ABCDEFHJKLMNPRSTUVWXY"
    date_and_individual_number_concatenated = id[0:6] + id[7:10]
    checksum_index: int = int(date_and_individual_number_concatenated) % 31
    return check_char_string[checksum_index] == id[-1]


def valitade_date(date: str) -> datetime | None:
    """
    Validates if the given date is a valid date.
    
    Args:
        date (str): The date to validate.
        
    Returns:
        datetime | None: datetime if the ID is valid, None otherwise.
    """
    date_format="%d.%m.%y"
    date_string = date[0:2] + "." + date[2:4] + "." + date[4:6]
    try:
        return datetime.strptime(date_string, date_format)
    except ValueError:
        return None
    

def valitade_id(id: str) -> datetime | None |bool:
    """
    Validates if the given ID is valid.
    
    Args:
        id (str): The ID to validate.
        
    Returns:
        bool: True if the ID is valid, False otherwise.
    """
    date = id[0:6]
    return valitade_date(date) and valitade_checksum(id)

    
def main() -> None:
    """
    Main function to test the date validation.
    """
    ids = ["230827-906F", "120488+246L", "310823A9877"]
    for id in ids:
        print(valitade_id(id))


if __name__ == "__main__":
    main()