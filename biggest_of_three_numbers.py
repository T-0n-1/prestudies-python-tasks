def luvuista_suurin(numero1: int, numero2: int, numero3: int) -> int | None:
    """
    Returns the largest of three numbers.
    """
    if numero1 > numero2 and numero1 > numero3:
        return numero1
    elif numero2 > numero1 and numero2 > numero3:
        return numero2
    elif numero3 > numero2 and numero3 > numero1:
        return numero3
    else:
        return None


def main():
    """
    Main function to get user input and print the largest number.
    """
    print("Anna kolme numeroa, niin ohjelma kertoo suurimman niistä.")
    
    numero1 = int(input("Anna ensimmäinen numero: "))
    numero2 = int(input("Anna toinen numero: "))       
    numero3 = int(input("Anna kolmas numero: "))
    
    suurin = luvuista_suurin(numero1, numero2, numero3)
    
    if suurin is not None:
        print(f"Suurin luku on {suurin}.")
    else:
        print("Kaikki kolme lukua ovat yhtä suuria.")


if __name__ == "__main__":
    main()
