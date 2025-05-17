def remove_smallest(lst: list[int]) -> None:
    """Remove the smallest number from the list and return the new list."""
    lst.remove(min(lst))
    

luvut = [2, 4, 6, 1, 3, 5]
remove_smallest(luvut)
print(luvut)
