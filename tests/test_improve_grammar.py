import pytest
from lib.improve_grammar import *


"""
Given an uncapitalised or punctuated string of a single word,
It returns False
"""
def test_improve_grammar_func_with_single_string():
    result = improve_grammar("hello")
    assert result == False


"""
Given a string with a punctuation at the end,
It returns True
"""
def test_improve_grammar_func_for_punctuation_mark():
    result = improve_grammar("how are you?")
    assert result == False


"""
Given a string with capitalised at the start
and punctuation at the end,
It returns True
"""
def test_improve_grammar_func_for_capital_and_punctuation_mark():
    result = improve_grammar("Hello world, how are you?")
    assert result == True


"""
Given an incorrect datatype (int) entered,
It returns a ValueError
"""
def test_improve_grammar_for_type_error():
    with pytest.raises(TypeError) as e:
        result = improve_grammar(123)
    error_message = str(e.value)
    assert error_message == "Input must be a string" 


"""
Given an empty string/value
It returns an Exception error
"""
def test_improve_grammar_for_empty_string_exception():
    with pytest.raises(Exception) as e:
        improve_grammar("")
    error_message = str(e.value)
    assert error_message == "Cannot enter an empty string"