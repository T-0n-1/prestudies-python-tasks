def digits_as_words() -> dict:
    """
    Create a dictionary with numbers from 0 to 99 as keys and their word representations as values.
    
    Returns:
        dict: A dictionary with numbers as keys and their word representations as values.
    """
    dictionary = {}
    
    numbers_from_zero_ten = {
        0: "nolla",
        1: "yksi",
        2: "kaksi",
        3: "kolme",
        4: "neljä",
        5: "viisi",
        6: "kuusi",
        7: "seitsemän",
        8: "kahdeksan",
        9: "yhdeksän",
        10: "kymmenen"
    }
    teens = "toista"    
    tens = "kymmentä"
    
    for i in range(0, 100):
        if i in range(0, 11):
            dictionary[i] = numbers_from_zero_ten[i]
        elif i in range(11, 20):
            dictionary[i] = numbers_from_zero_ten[i % 10] + teens
        elif i in range(20, 100):
            if i % 10 == 0:
                dictionary[i] = numbers_from_zero_ten[i // 10] + tens
            else:
                dictionary[i] = numbers_from_zero_ten[i // 10] + tens + numbers_from_zero_ten[i % 10]
    return dictionary


luvut = digits_as_words()
print(luvut[2])
print(luvut[11])
print(luvut[45])
print(luvut[99])
print(luvut[0])