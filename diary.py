from pathlib import Path


def read_entries(path: Path) -> None:
    """
    Read and print diary entries from the file.

    :param path: Path to the diary file.
    """
    print("Merkinnät: ")
    if path.exists():
        print(path.read_text())
    else:
        print("Ei merkintöjä, lisää ensin merkintä.")


def add_entry(path: Path) -> None:
    """
    Add a diary entry to the file.

    :param path: Path to the diary file.
    """
    with path.open("a") as diary:
        diary.write(input("Anna merkintä: ") + "\n")
        print("Päiväkirja tallennettu\n")


def user_interface(path: Path) -> None:
    """
    User interface for the diary application.

    :param path: Path to the diary file.
    """
    while True:
        user_input = input("1 - lisää merkintä, 2 - lue merkinnät, 0 - lopeta\nValinta: ")
        if user_input == "1":
            add_entry(path)
        elif user_input == "2":
            read_entries(path)
        elif user_input == "0":
            print("Heippa!\n")
            break
        else:
            print("Virheellinen valinta, yritä uudelleen.\n")
            continue


def define_path() -> Path:
    """
    Define the path to the diary file.
    """
    return Path("diary.txt")


def main() -> None:
    """
    Main function to run the diary application.
    """
    path = define_path()
    user_interface(path)


if __name__ == "__main__":
    main()
    