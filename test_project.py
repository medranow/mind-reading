from project import threeTrick, divideTrick, luckyNumber, get_trick
import pytest

def test_threeTrick(monkeypatch):
    # Test for entering a number btw 1 and 10
    monkeypatch.setattr('builtins.input', lambda _: "3")
    number = int(input("Choose a number between 1 and 10: "))
    assert number == 3

    # Test for entering a string
    with pytest.raises(ValueError):
        monkeypatch.setattr('builtins.input', lambda _: "b")
        number = int(input("Choose a number between 1 and 10: "))


def test_divideTrick(monkeypatch):
    # Test for entering a number btw 1 and 10
    monkeypatch.setattr('builtins.input', lambda _: "3")
    number = int(input("Choose a number between 1 and 10: "))
    assert number == 3

    # Test for entering a string
    with pytest.raises(ValueError):
        monkeypatch.setattr('builtins.input', lambda _: "b")
        number = int(input("Choose a number between 1 and 10: "))

def test_luckyNumber(monkeypatch):
    # Test for entering a number btw 1 and 10
    monkeypatch.setattr('builtins.input', lambda _: "3")
    number = int(input("Choose a number between 1 and 10: "))
    assert number == 3

    # Test for entering a string
    with pytest.raises(ValueError):
        monkeypatch.setattr('builtins.input', lambda _: "b")
        number = int(input("Choose a number between 1 and 10: "))


def test_get_trick(monkeypatch):
    with pytest.raises(ValueError):
        monkeypatch.setattr('builtins.input', lambda _: "b")
        number = int(input("Choose a number between 1 and 10: "))

    monkeypatch.setattr('builtins.input', lambda _: "3")
    number = int(input("Choose a number between 1 and 10: "))
    assert number == 3