import pytest
from lib.say_hello import say_hello

"""
testt say hello func to debug the func before
10 min timer goes off.
The issue was "f" string was missing which
generated an "Assertion error"
"""

def test_say_hello_func_with_string():
    result = say_hello("kay")
    assert result == "hello kay"

def test_say_hello_func_with_empty_string():
    result = say_hello("")
    assert result == "hello "