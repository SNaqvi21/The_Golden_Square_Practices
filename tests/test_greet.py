from lib.greet import *

def test_greet():
    result = greet("Pablo")
    assert result == "Hello, Pablo!"

