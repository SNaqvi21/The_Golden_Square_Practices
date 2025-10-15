import pytest
from lib.diary_entry import DiaryEntry

"""
Given an empty (title: content)
Raises an error
"""
def test_diary_entry_class_with_empty_string_error():
    with pytest.raises(Exception) as e:
        diary_entry = DiaryEntry("", "")
    error_message = str(e.value)
    assert error_message == "Contents should not be empty!"


"""
Given a single diary entry (title: content)
It returns it in the correct format
"My Title: These are the contents"
"""
def test_diary_entry_class_for_a_single_entry():
    diary_entry = DiaryEntry("My Title", "These are the contents")
    result = diary_entry.format()
    assert result == "My Title: These are the contents"


"""
Given a single diary entry (title: content)
count_words returns the number of words in an int data type
"""
def test_diary_entry_class_with_count_words_method():
    diary_entry = DiaryEntry("My Title", "These are the contents")
    result = diary_entry.count_words()
    assert result == 6


"""
Given 2 words
reading_time(2) Returns an estimate of the reading time 
in minutes for the contents
"""
def test_diary_entry_class_with_reading_time_wpm_given_two_words():
    diary_entry = DiaryEntry("My Title", "This content")
    result = diary_entry.reading_time(2)
    assert result == 1


"""
Given 4 words
reading_time(2) Returns an estimate of the reading time 
in minutes for the contents
"""
def test_diary_entry_class_with_reading_time_wpm_given_four_words():
    diary_entry = DiaryEntry("My Title", "One two three four")
    result = diary_entry.reading_time(2)
    assert result == 2


"""
Given 3 words 
reading_time(2) Returns an estimate of the reading time 
in minutes for the contents
"""
def test_diary_entry_class_with_reading_time_wpm_given_three_words():
    diary_entry = DiaryEntry("My Title", "One two three")
    result = diary_entry.reading_time(2)
    assert result == 2


"""
Given 0 words 
it raises an error
"""
def test_diary_entry_class_with_reading_time_0_wpm_raises_error():
    diary_entry = DiaryEntry("My Title", "One two three")
    with pytest.raises(Exception) as e:
        result = diary_entry.reading_time(0)
    error_message = str(e.value)
    assert error_message == "Value of wpm should not be 0"


"""
Given empty contents
it raises an error
"""
def test_diary_entry_class_with_reading_time_empty_contents():
    with pytest.raises(Exception) as e:
        diary_entry = DiaryEntry("", "")
    error_message = str(e.value)
    assert error_message == "Contents should not be empty!"


"""
Given a contents of 6 words
and a wpm 2
and minutes 2
reading_chunk returns the first two words 
or reading content read in the given num of minutes
"""
def test_diary_entry_class_with_reading_chunk_method_with_one_word():
    diary_entry = DiaryEntry("My Title", "one two three four five six")
    result = diary_entry.reading_chunk(2, 1)
    assert result == "one two"


"""
Given a contents of 6 words
and a wpm 2
and minutes 2
reading_chunk returns the first four words 
or reading content read in the given num of minutes
"""
def test_diary_entry_class_with_reading_chunk_method_with_one_word():
    diary_entry = DiaryEntry("My Title", "one two three four five six")
    result = diary_entry.reading_chunk(2, 2)
    assert result == "one two three four"



"""
Given a contents of 6 words
and a wpm 2
and minutes 1
reading_chunk returns the first 2 "one two" words 
next time it returns "three four"
or reading content read in the given num of minutes
"""
def test_diary_entry_class_with_reading_chunk_method_with_two_words_then_repeat():
    diary_entry = DiaryEntry("My Title", "one two three four five six")
    result = diary_entry.reading_chunk(2, 1)
    assert result == "one two"
    result = diary_entry.reading_chunk(2, 1)
    assert result == "three four"