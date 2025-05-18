class PersonInPhonebook:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = [phone_number]

    def __str__(self):
        information = f"{self.name}: "
        for number in self.phone_number:
            information += f"\n{number}"
        return information


class PhoneBook:
    def __init__(self):
        self.phonebook = {}
    
    def __str__(self):
        information = "LUETTELO: "
        for person in self.phonebook:
            information += f"\n{person}"
        return information
    
    def prompt_name(self) -> str:
        """
        Prompt the user for a name.
        """
        name = input("Anna nimi: ")
        return name

    def prompt_number(self) -> str:
        """
        Prompt the user for a phone number.
        """
        number = input("Anna numero: ")
        return number

    def add_information(self, name, phone_number):
        """
        Add a new name and phone number to the phonebook or add new number to existing name.
        """
        if name in self.phonebook:
            self.phonebook[name].phone_number.append(phone_number)
        else:
            self.phonebook[name] = PersonInPhonebook(name, phone_number)
        print("Ok!")

    def search_name(self, name):
        """
        Search for a name in the phonebook.
        
        Args:
            name (str): The name to search for.
        """         
        if name in self.phonebook:
            print(self.phonebook[name])
        else:
            print(f"Nimi: {name}")
            print("ei numeroa")




def user_command() -> None:
    """
    Prompt the user for command and act depending on it.
    """
    phonebook = PhoneBook()
    while True:
        user_input = input("komento (1 hae, 2 lisää, 3 tulosta, 4 lopeta): ")
        if user_input == "1":
            name = phonebook.prompt_name()
            phonebook.search_name(name)
        elif user_input == "2":
            name = phonebook.prompt_name()
            number = phonebook.prompt_number()
            phonebook.add_information(name, number)
        elif user_input == "3":
            print(phonebook)
        elif user_input == "4":
            print("Lopetetaan...")
            break
        else:
            continue


def main() -> None:
    """
    Main function to execute the program.
    """
    user_command()


if __name__ == "__main__":
    main()