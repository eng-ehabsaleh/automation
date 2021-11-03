from automation.automation import numbers,email


def test_numbers():
    actual = numbers()
    excepted = open("phone_numbers.txt", "r").read()
    assert actual == excepted


def test_email():
    actual = email()
    excepted = open("emails.txt", "r").read()
    assert actual == excepted