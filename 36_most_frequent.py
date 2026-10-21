def most_frequent(lst: list):
    if not lst:
        return None
    return max(set(lst), key=lst.count)
