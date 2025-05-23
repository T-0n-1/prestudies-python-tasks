from random import choice

noppa = {"A": [3, 3, 3, 3, 3, 6],
         "B": [2, 2, 2, 5, 5, 5],
         "C": [1, 4, 4, 4, 4, 4]}
    

def roll_two_dices(dice1: str, dice2: str) -> tuple:
    """
    Simulate rolling two types of dice a specified number of times.
    :param dice1: The first type of dice to roll.
    :param dice2: The second type of dice to roll.
    :return: A tuple containing the results of the rolls.
    """
    result1 = choice(noppa[dice1])
    result2 = choice(noppa[dice2])
    results = result1, result2
    return results


def play_dice_game(dice1: str, dice2: str, times: int) -> tuple[int, int, int]:
    """
    Count the results of rolling two types of dice.
    :return: A tuple containing the counts of each result 
        (wins for dice1, wins for dice2, ties).
    """
    wins1 = 0
    wins2 = 0
    ties = 0
    for _ in range(times):
        result = roll_two_dices(dice1, dice2)
        if result[0] > result[1]:
            wins1 += 1
        elif result[0] < result[1]:
            wins2 += 1
        else:
            ties += 1
    return wins1, wins2, ties


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
    print()
    tulos = play_dice_game("A", "C", 1000)
    print(tulos)
    tulos = play_dice_game("B", "B", 1000)
    print(tulos)


if __name__ == "__main__":
    main()