import string

def is_pangram(s: str) -> bool:
    alphabet = set(string.ascii_lowercase)
    return alphabet.issubset(set(s.lower()))
