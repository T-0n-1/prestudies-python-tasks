from datetime import date


def years_from_datelist(dates: list[date]) -> list[date.year]:
    """
    Convert a list of date strings into a list of years.

    : param dates (list[str]): A list of date strings in the format 'YYYY-MM-DD'.
    : return: A list of years extracted from the date strings.
    """
    return [date.year for date in dates]


def main():
    """
    Main function to demonstrate the conversion of date strings to years.
    """
    paiva1 = date(2019, 2, 3)
    paiva2 = date(2006, 10, 10)
    paiva3 = date(1993, 5, 9)

    vuodet = years_from_datelist([paiva1, paiva2, paiva3])
    print(vuodet)


if __name__ == "__main__":
    main()