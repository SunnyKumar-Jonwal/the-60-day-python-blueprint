def reverse_string(text):
    return text[::-1]


def test_reverse_normal_word():
    assert reverse_string("hello") == "olleh"


def test_reverse_empty_string():
    assert reverse_string("") == ""
