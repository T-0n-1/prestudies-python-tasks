from random import choice

noppa = {"A": [3, 3, 3, 3, 3, 6],
         "B": [2, 2, 2, 5, 5, 5],
         "C": [1, 4, 4, 4, 4, 4]}


def roll_dice(dice: str) -> int:
    """
    Simulate rolling a dice.
    :param dice: The type of dice to roll.
    :return: The result of the dice roll.
    """
    return choice(noppa[dice])

def main():
    """
    Main function to demonstrate dice rolling.
    """
    for i in range(20):
        print(roll_dice("A"), " ", end="")
    print()
    for i in range(20):
        print(roll_dice("B"), " ", end="")
    print()
    for i in range(20):
        print(roll_dice("C"), " ", end="")


if __name__ == "__main__":
    main()