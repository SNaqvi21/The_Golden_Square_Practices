from lib.report_length import *

# It returns length of string with spaces:
def test_string_with_whitespaces_in_report_length():
    result = report_length(" Hello  World ")
    assert result == "This string was 14 characters long."

# It returns length of empty string:
def test_empty_string_in_report_length():
    result = report_length("")
    assert result == "This string was 0 characters long."

# It returns length of short string:
def test_short_string_in_report_length():
    result = report_length("Dog")
    assert result == "This string was 3 characters long."

# It returns length of long string:
def test_long_string_in_report_length():
    result = report_length("Supercalafragilisticexpialadocious")
    assert result == "This string was 34 characters long."

# It retruns length of special characters string:
def test_special_chars_length_in_report_length():
    result = report_length("£@!_-%")
    assert result == "This string was 6 characters long."