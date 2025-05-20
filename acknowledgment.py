from pathlib import Path


def write_acknowledgment(name: str, file_path: Path) -> None:
    """
    Print the acknowledgment message.
    """
    message = f"Hei {name}, toivomme viihtyisiä hetkiä python-kurssimateriaalin parissa!\nTerveisin mooc.fi-tiimi"
    file_path.write_text(message)


def define_file_path(file_path: str) -> Path:
    """
    Define the file path.
    """
    return Path(file_path)
    

def prompt_user() -> tuple:
    """
    Prompt the user for their name and file path.
    """
    name = input("Kenelle teos omistetaan: ")
    file = input("Mihin kirjoitetaan: ")
    return name, file


def main() -> None:
    """
    Main function to execute the program.
    """
    name, file_path = prompt_user()
    file_path = define_file_path(file_path)
    write_acknowledgment(name, file_path)


if __name__ == "__main__":
    main()