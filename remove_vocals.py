def remove_vocals(string: str) -> str:
    """
    Remove vocals from a string.
    
    Parameters:
    string (str): String to remove vocals from.
    """
    vocals = "aeiouyäöå"
    for char in string:
        if char in vocals:
            string = string.replace(char, "")
    return string
    

def main() -> None:
    """
    Main function to execute the program.
    """
    jono = "Tämä on esimerkki"

    print(f"Jono: {jono} ja ilman vokaaleja: {remove_vocals(jono)}")


if __name__ == "__main__":
    main()