lst: list[int] = []


def remove_from_list(lst: list) -> list:
    """
    Remove the last element from the list.
    """
    if lst:
        lst.pop()
    return lst

def add_to_list(list: list) -> list:
    """
    Add a new element to the list.
    """
    if not list:
        list.append(1)
    else:
        list.append(list[-1] + 1)
    return list


def main() -> None:
    """
    Main function to execute the program.
    """
    while True:
        print(f"Lista on nyt {list}")
        prompt = input("(l)isää, (p)oista vai e(x)it: ")
        if prompt == "l":
            add_to_list(lst)
        elif prompt == "p":
            remove_from_list(lst)
        elif prompt == "x":
            print("Moi!")
            break
    

if __name__ == "__main__":
    main()