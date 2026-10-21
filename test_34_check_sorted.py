import importlib
module = importlib.import_module("34_check_sorted")

def test_is_sorted():
    assert module.is_sorted([1, 2, 3, 4, 5]) is True
    assert module.is_sorted([5, 4, 3, 2, 1]) is True
    assert module.is_sorted([1, 3, 2, 4]) is False
