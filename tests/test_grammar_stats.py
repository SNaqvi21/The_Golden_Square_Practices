import pytest
from lib.grammar_stats import GrammarStats

"""
Given an capitalised and punctuated string 
of a word,
It returns True
"""
def test_grammar_stats_class_with_single_word():
    gs = GrammarStats()
    result = gs.check("Hello world.")
    assert result == True


"""
Given an uncapitalised and unpunctuated string 
of a word,
It returns False
"""
def test_grammar_stats_class_with_unformatted_single_word():
    gs = GrammarStats()
    result = gs.check("hello world")
    assert result == False

"""
Given a capitalised but upunctuated string 
of a word,
It returns False
"""
def test_grammar_stats_class_with_without_punctuation_of_single_word():
    gs = GrammarStats()
    result = gs.check("hello world")
    assert result == False


"""
# Given a capitalised and punctuated string 
# of a word,
# test percentage method
"""
def test_grammar_stats_class_percentage_good_method():
    gs = GrammarStats()
    gs.check("Hello!")
    gs.check("hello world")
    result = gs.percentage_good()
    assert result == 50

"""
# Given a capitalised and punctuated string 
# of a word,
# test percentage method
"""
def test_grammar_stats_class_percentage_good_method_hundred_percent():
    gs = GrammarStats()
    gs.check("Hello!")
    gs.check("Hello world, how are you?")
    result = gs.percentage_good()
    assert result == 100

"""
# Given an empty string is passed
# raise error
"""
def test_grammar_stats_class_for_empty_string_exception_error():
    gs = GrammarStats()
    with pytest.raises(Exception) as e:
        gs.check("")
    error_message = str(e.value)
    assert error_message == "Cannot enter an empty string"


"""
# Given an incorrect value entered is passed
# raise error
"""
def test_grammar_stats_class_with_type_error():
    gs = GrammarStats()
    with pytest.raises(TypeError) as e:
        gs.check(123)
    error_message = str(e.value)
    assert error_message == "Input must be a string"
