from lib.check_codeword import *

# Test if codeword Returns "Correct! Come in"
def test_check_codeword_for_horse():
    result = check_codeword("horse")
    assert result == "Correct! Come in."

# If the codeword is wrong, Returns "WRONG!"
def test_for_incorrect_codeword():
    result = check_codeword("Diego")
    assert result == "WRONG!"

# If the codeword is correct first and last letter,
# Returns "Close, but nope."
def test_codeword_correct_first_and_last_letter():
    result = check_codeword("house")
    assert result == "Close, but nope."

# If codeword has right first letter but wrong last letter
def test_codeword_correct_first_letter_wrong_last_letter():
    result = check_codeword("hello")
    assert result == "WRONG!"

# If codeword has WRONG first letter but RIGHT last letter
def test_codeword_wrong_first_letter_right_last_letter():
    result = check_codeword("mouse")
    assert result == "WRONG!"