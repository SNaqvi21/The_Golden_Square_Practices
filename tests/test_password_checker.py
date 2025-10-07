import pytest
from lib.password_checker import PasswordChecker

# check initial state
def test_initial_state_of_password_checker_class():
    password_checker = PasswordChecker()
    with pytest.raises(Exception) as e:
        password_checker.check("")
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."

# check correct password length
def test_correct_length_password_checker_class():
    password_checker = PasswordChecker()
    result = password_checker.check("password")
    assert result == True

# check error/exception
def test_error_exception_of_password_checker_class():
    password_checker = PasswordChecker()
    with pytest.raises(Exception) as e:
        password_checker.check("passwor")
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."


# check with whitespace
def test_error_with_whitespace_of_password_checker_class():
    password_checker = PasswordChecker()
    with pytest.raises(Exception) as e:
        password_checker.check("       ")
    assert str(e.value) == "Invalid password, must be 8+ characters."
