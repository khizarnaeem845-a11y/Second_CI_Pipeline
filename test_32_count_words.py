import importlib
module = importlib.import_module("32_count_words")

def test_count_words_standard():
    assert module.count_words("Hello world this is a test") == 6

def test_count_words_empty():
    assert module.count_words("") == 0
