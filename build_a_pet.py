class Lemmikki:
    def __init__(self, nimi: str, laji: str, syntymavuosi: int):
        self.nimi = nimi
        self.laji = laji
        self.syntymavuosi = syntymavuosi

    def __str__(self):
        return f"{self.nimi} ({self.laji}, {self.syntymavuosi})"
    

def uusi_lemmikki(nimi: str, laji: str, syntymavuosi: int) -> Lemmikki:
    """
    Luo uuden lemmikin.

    :param nimi: Lemmikin nimi
    :param laji: Lemmikin laji
    :param syntymavuosi: Lemmikin syntymävuosi
    :return: Uusi Lemmikki-olio
    """
    return Lemmikki(nimi, laji, syntymavuosi)

    
def main():
    """
    Pääohjelma, joka luo uuden lemmikin ja tulostaa sen tiedot.
    """
    musti = uusi_lemmikki("Musti", "koira", 2017)
    print(musti.nimi)
    print(musti.laji)
    print(musti.syntymavuosi)


if __name__ == "__main__":
    main()