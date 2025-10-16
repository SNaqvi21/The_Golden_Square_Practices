import pytest
from lib.phonebook_recorder import PhonebookRecorder


"""
Given an empty record
It returns an initial state
"""
def test_phonebook_recorder_class_initial_state():
    pr = PhonebookRecorder()
    result = pr.get_number()
    assert result == []

"""
Given an entry with no numbers,
It returns list with no nums
"""
def test_phonebook_recorder_class_with_no_numbers():
    pr = PhonebookRecorder()
    pr.add_number("No numbers")
    result = pr.get_number()
    assert result == []

"""
Given an entry with one phone number + other info,
It returns just the number correctly in a list
"""
def test_phonebook_recorder_class_with_one_number_mixed_with_information():
    pr = PhonebookRecorder()
    pr.add_number("call pablo 123-456-78910")
    result = pr.get_number()
    assert result == ["12345678910"]


"""
Given multiple entries
It returns the unique numbers list correctly"""
def test_phonebook_recorder_class_with_multiple_entries_and_duplicates():
    pr = PhonebookRecorder()
    pr.add_number("call diego 10987654321 and then vincezo 51412110313 and then call pablo 23412378911")
    pr.add_number("call pablo again 23412378911")
    result = pr.get_number()
    assert result == ["10987654321", "23412378911", "51412110313"]
    # sorted() returns numbers alphabetically ("109.." < "234..." < "514...") If test expects
    # a different order (insertion order) it will fail

"""
Given an empty record entry,
It returns exception
"""
def test_phonebook_recorder_class_with_empty_string_entry():
    pr = PhonebookRecorder()
    with pytest.raises(Exception) as e:
        pr.add_number("")
    error_message = str(e.value)
    assert error_message == "Entry should not be empty"


"""
Given an invalid entry,
It returns type error
"""
# def test_phonebook_recorder_class_with_empty_string_entry():
#     pr = PhonebookRecorder()
#     with pytest.raises(TypeError) as e:
#         pr.add_number("gijgjgogoogkggkgj 986686")
#     error_message = str(e.value)
#     assert error_message == "Entry must be an 11-digit number"