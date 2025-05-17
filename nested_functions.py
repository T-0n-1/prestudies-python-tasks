def tervehdi(nimi: str) -> None:
    print(f"Moikka {nimi}!")


def tervehdi_monesti(nimi: str, kerroin: int) -> None:
    for x in range(kerroin):
        tervehdi(nimi)


if __name__ == "__main__":
    tervehdi_monesti("Matti", 3)
    tervehdi_monesti("Maija", 5)