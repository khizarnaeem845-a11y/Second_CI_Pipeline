import importlib
module = importlib.import_module("38_missing_number_xor")

def test_find_missing_number():
    assert module.find_missing_number([1, 2, 4, 5], 5) == 3
