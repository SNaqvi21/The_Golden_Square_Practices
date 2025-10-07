import pytest
from lib.present import Present

# testing wrap()error/exception

def test_wrap_error_and_exception_of_present_class():
    present = Present()
    present.wrap("cologne") # first wrap is fine
    with pytest.raises(Exception) as e:
        present.wrap("book") # second wrap will raise error
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped."

# testing unwrap() error/exception 
def test_unwrap_error_and_exception_of_present_class():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    error_message = str(e.value)
    assert error_message == "No contents have been wrapped."