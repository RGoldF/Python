import pytest
from string_utils import StringUtils

string_utils = StringUtils()


@pytest.mark.positive_test
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative_test
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive_test
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),
    ("   Hello world", "Hello world"),
    ("   %python", "%python"),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative_test
@pytest.mark.parametrize("input_str, expected", [
    ("   ", ""),
    ("Hello world", "Hello world"),
    (" Sky Pro ", "Sky Pro "),
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.positive_test
@pytest.mark.parametrize("string, symbol, expected", [
    ("skypro", "s", True),
    ("123abc", "3a", True),
    ("Hello world", "world", True),
])
def test_contains_positive(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected


@pytest.mark.negative_test
@pytest.mark.parametrize("string, symbol, expected", [
    ("skypro", "$", False),
    ("123abc", "4a", False),
    ("Hello", "olleH", False),
])
def test_contains_negative(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected


@pytest.mark.positive_test
@pytest.mark.parametrize("string, symbol, expected", [
    ("Sky Pro", " ", "SkyPro"),
    ("hello world", "hello", " world"),
    ("123abc", "123", "abc"),
])
def test_delete_symbol_positive(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected


@pytest.mark.negative_test
@pytest.mark.parametrize("string, symbol, expected", [
    ("Skyeng", "E", "Skyeng"),
    ("", "p", ""),
    ("$kyPro", "s", "$kyPro"),
])
def test_delete_symbol_negative(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected
