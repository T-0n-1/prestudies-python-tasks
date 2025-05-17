def viiva(kuvio: str, kerroin: int) -> None:
    """
    Funktio tulostaa annetun kuvion useita kertoja.

    Args:
        kuvio (str): Tulostettava kuvio.
        kerroin (int): Kuinka monta kertaa kuvio tulostetaan.
    """
    
    for i in range(kerroin):
        print(kuvio, end=' ')
    print()


def kuvio(kuvio1: str, kerroin1: int, kuvio2: str, kerroin2: int) -> None:
    """
    Funktio tulostaa kuvion, jonka yläosana on kahden ensimmäisen parametrin 
    määrittelemä kolmio ja alaosana ensimmäisen ja kahden jälkimmäisen parametrin 
    määrittelemä suorakulmio.

    Args:
        kuvio1 (str): Ensimmäinen kuvio.
        kerroin1 (int): Ensimmäisen kuvion kerroin.
        kuvio2 (str): Toinen kuvio.
        kerroin2 (int): Toisen kuvion kerroin.
    """
    for i in range(kerroin1):
        viiva(kuvio1, i+1)
    for i in range(kerroin2):
        viiva(kuvio2, kerroin1)


if __name__ == "__main__":
    kuvio('*', 5, '#', 3)
    print()
    kuvio('X', 4, 'O', 2)
    print()
    kuvio('A', 3, 'B', 1)
    