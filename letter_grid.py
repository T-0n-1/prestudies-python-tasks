def print_letter_grid(grid_list: list) -> None:
    """
    Print the letter grid.
    
    :param grid_list: The list of letters to print.
    """
    for list in grid_list:
        print(" ".join(list))


def build_letter_grid(level_given: int) -> list:
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    grid = []
    for level in range(level_given):
        letter = alphabets[level]

        if level == 0:
            grid.append([letter])
        else:
            for row in grid:
                row.insert(0, letter)
                row.append(letter)
            new_row = [letter] * (2 * level + 1)
            grid.insert(0, new_row)
            grid.append(new_row[:])
    return grid


def prompt_user_for_level() -> int:
    """
    Prompt the user for the level of the letter grid.
    
    :return: The level of the letter grid.
    """
    while True:
        try:
            level = int(input("Kerroksia: "))
            if level < 1 or level > 26:
                raise ValueError("Kerroksien määrä on oltava välillä 1-26.")
            return level
        except ValueError as e:
            print(f"Virheellinen syöte: {e}. Yritä uudelleen.")
        

def main() -> None:
    """
    Main function to execute the program.
    """
    kerroksia = prompt_user_for_level()
    letter_grid = build_letter_grid(kerroksia)
    print_letter_grid(letter_grid)


if __name__ == "__main__":
    main()