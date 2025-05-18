phonebook: dict = {}


def prompt_name() -> str:
    """
    Prompt the user for a name.
    """
    name = input("Anna nimi: ")
    return name


def add_information() -> None:
    """
    Add a new name and phone number to the phonebook or add new number to existing name.
    """
    nimi = prompt_name()
    numero = input("Anna puhelinnumero: ")
    if nimi in phonebook:
        phonebook[nimi].append(numero)
    else:
        phonebook[nimi] = [numero]
    print("Ok!")
    

def search_name() -> None:
    """
    Search for a name in the phonebook.
    
    Args:
        name (str): The name to search for.
    """
    nimi = prompt_name()
    print(f"Nimi: {nimi}")
    if nimi in phonebook:
        for number in phonebook[nimi]:
            print(f"{number}")
    else:
        print("ei numeroa")


def user_command() -> None:
    """
    Prompt the user for command and act depending on it.
    """
    while True:
        user_input = input("komento (1 hae, 2 lisää, 3 lopeta): ")
        if user_input == "1":
            search_name()
        elif user_input == "2":
            add_information()
        elif user_input == "3":
            print("Lopetetaan...")
            break


def main() -> None:
    """
    Main function to execute the program.
    """
    user_command()


if __name__ == "__main__":
    main()