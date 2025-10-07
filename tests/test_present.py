import pytest
from lib.present import Present

# check initial state
def test_initial_state():
    present = Present()
    assert present.__init__() == None

# check wrap()error/exception
def test_wrap_error_and_exception_of_present_class():
    present = Present()
    present.wrap("cologne") # first wrap is fine
    with pytest.raises(Exception) as e:
        present.wrap("book") # second wrap will raise error
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped."

# check unwrap() error/exception 
def test_unwrap_error_and_exception_of_present_class():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    error_message = str(e.value)
    assert error_message == "No contents have been wrapped."

# check successful wrap() then unwrapping().
def test_successful_wrap_and_unwrap_methods_of_present_class():
    present = Present()
    present.wrap("toy")
    present.unwrap()
    assert present.unwrap() == "toy"

# check error when unwrap() called before wrap()
def test_unwrap_before_wrap_method_of_present_class():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    error_message = str(e.value)
    assert error_message == "No contents have been wrapped."

# check multiple instances
def test_multiple_instances_of_present_class():
    present1 = Present()
    present2 = Present()
    present1.wrap("christmas socks")
    assert present1.unwrap() == "christmas socks"
    with pytest.raises(Exception) as e:
        present2.unwrap()
    error_message = str(e.value)
    assert error_message == "No contents have been wrapped."
    