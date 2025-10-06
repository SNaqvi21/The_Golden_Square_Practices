from lib.counter import *

# tests for postiive int
def test_to_check_positive_number_in_counter_class():
    counter = Counter()
    counter.add(14)
    assert counter.report() == "Counted to 14 so far."

# tests for negative int
def test_to_check_negative_number_in_counter_class():
    counter = Counter()
    counter.add(-14)
    assert counter.report() == "Counted to -14 so far."
    
# tests starts at 0
def test_to_check_counter_starts_at_0_in_counter_class():
    counter = Counter()
    assert counter.report() == "Counted to 0 so far."

# test to check add two postive nums
def test_to_check_two_postive_nums_add_in_counter_class():
    counter = Counter()
    counter.add(5)
    counter.add(9)
    assert counter.report() == "Counted to 14 so far."

# test to add two negative nums
def test_adding_two_negative_nums_in_counter_class():
    counter = Counter()
    counter.add(-5)
    counter.add(-9)
    assert counter.report() == "Counted to -14 so far."

#  test to check if intial state is 0
def test_to_check_initial_state_in_counter_class():
    counter = Counter()
    assert counter.report() == "Counted to 0 so far."

# test report after adding
def test_report_method_after_adding_in_counter_class():
    counter = Counter()
    counter.add(8)
    counter.add(4)
    assert counter.report() == "Counted to 12 so far."



