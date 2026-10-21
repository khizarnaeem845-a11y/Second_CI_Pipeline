import importlib
module = importlib.import_module("37_rotate_string")

def test_rotate_string():
    assert module.rotate_string("abcdef", 2) == "efabcd"
    assert module.rotate_string("hello", 0) == "hello"
