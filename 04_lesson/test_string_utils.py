import pytest
from string_utils import StringUtils


@pytest.fixture
def utils():
    return StringUtils()


# --- capitalize ---
def test_capitalize_positive(utils):
    assert utils.capitalize("skypro") == "Skypro"


def test_capitalize_already_capital(utils):
    assert utils.capitalize("Skypro") == "Skypro"


def test_capitalize_empty(utils):
    assert utils.capitalize("") == ""


def test_capitalize_numbers(utils):
    assert utils.capitalize("123abc") == "123abc"


def test_capitalize_none(utils):
    with pytest.raises(AttributeError):
        utils.capitalize(None)


# --- trim ---
def test_trim_positive(utils):
    assert utils.trim("   skypro") == "skypro"


def test_trim_no_spaces(utils):
    assert utils.trim("skypro") == "skypro"


def test_trim_only_spaces(utils):
    assert utils.trim("   ") == ""


def test_trim_empty(utils):
    assert utils.trim("") == ""


def test_trim_none(utils):
    with pytest.raises(AttributeError):
        utils.trim(None)


# --- contains ---
def test_contains_positive(utils):
    assert utils.contains("SkyPro", "S") is True


def test_contains_negative(utils):
    assert utils.contains("SkyPro", "U") is False


def test_contains_empty_string(utils):
    assert utils.contains("", "a") is False


def test_contains_empty_symbol(utils):
    assert utils.contains("SkyPro", "") is False


def test_contains_none(utils):
    with pytest.raises(AttributeError):
        utils.contains(None, "a")


# --- delete_symbol ---
def test_delete_symbol_positive(utils):
    assert utils.delete_symbol("SkyPro", "k") == "SyPro"


def test_delete_symbol_substring(utils):
    assert utils.delete_symbol("SkyPro", "Pro") == "Sky"


def test_delete_symbol_not_found(utils):
    assert utils.delete_symbol("SkyPro", "Z") == "SkyPro"


def test_delete_symbol_empty(utils):
    assert utils.delete_symbol("", "a") == ""


def test_delete_symbol_none(utils):
    with pytest.raises(AttributeError):
        utils.delete_symbol(None, "a")
