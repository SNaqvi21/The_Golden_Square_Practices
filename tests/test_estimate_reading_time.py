import pytest
from lib.estimate_reading_time import estimate_reading_time

"""
Given a text of 200 words,
It returns 1.0
"""
def test_estimate_reading_time_with_two_hundred_words():
    text = " ".join(["words" for i in range (0,200)])
    result = estimate_reading_time(text)
    assert result == 1.0

"""
Given a text of 400 words,
It returns 2.0
"""
def test_estimate_reading_time_with_four_hundred_words():
    text = " ".join("words" for i in range(0,400))
    result = estimate_reading_time(text)
    assert result == 2.0

"""
Given a text of 10 words,
It returns 0.05
"""
def test_estimate_reading_time_with_ten_words():
    result = estimate_reading_time("Hello Wolrd Hello World Hello World Hello World hello World")
    assert result == 0.05

"""
Given a text of 300 words,
It returns 1.5
"""
def test_estimate_reading_time_with_three_hundred_fifty_words():
    text = " ".join(["words" for i in range (0, 300)])
    result = estimate_reading_time(text)
    assert result == 1.5

"""
Given a text of 200 words,
It returns 1.0
"""
def test_estimate_reading_time_with_empty_string():
    with pytest.raises(Exception) as e:
        estimate_reading_time("")
    error_message = str(e.value)
    assert error_message == "Empty string cannot be estimated!"