def samat(merkkijono: str, indeksi1: int, indeksi2: int) -> bool:
    """
    Funktio tarkistaa, onko merkkijonossa indeksi1 ja indeksi2 sama merkki.
    """
    if indeksi1 < 0 or indeksi2 < 0 or indeksi1 >= len(merkkijono) or indeksi2 >= len(merkkijono):
        raise ValueError("Indeksit eivät saa olla negatiivisia tai ylittää merkkijonon pituutta.")
    return merkkijono[indeksi1] == merkkijono[indeksi2]


def main():
    """
    Pääohjelma, joka kysyy käyttäjältä merkkijonon ja kaksi indeksiä.
    """
    merkkijono = input("Anna merkkijono: ")
    indeksi1 = int(input("Anna ensimmäinen indeksi: "))
    indeksi2 = int(input("Anna toinen indeksi: "))
    try:
        if samat(merkkijono, indeksi1, indeksi2):
            print(f"Merkit {indeksi1} ja {indeksi2} ovat samat.")
        else:
            print(f"Merkit {indeksi1} ja {indeksi2} eivät ole samat.")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()