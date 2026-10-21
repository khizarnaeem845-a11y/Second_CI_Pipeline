def is_sorted(lst: list) -> bool:
    return lst == sorted(lst) or lst == sorted(lst, reverse=True)
