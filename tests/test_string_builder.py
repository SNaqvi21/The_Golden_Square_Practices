from lib.string_builder import *

# test to check initial state
def test_to_check_initial_state_in_string_builder_class():
    string_builder = StringBuilder()
    assert string_builder.output() == ""
    assert string_builder.size() == 0

# test empty string
def test_empty_string_in_string_builder_class():
    string_builder = StringBuilder()
    string_builder.add("")
    assert string_builder.size() == 0
    assert string_builder.output() == ""

# test to check if add() method adds stirng
def test_adding_two_strings_in_string_builder_class():
    string_builder = StringBuilder()
    string_builder.add("Hello,")
    string_builder.add("World")
    assert string_builder.output() == "Hello,World"
    assert string_builder.size() == 11

# test to check size() method returns len of string
def test_size_method_in_string_builder_class():
    string_builder = StringBuilder()
    string_builder.add("Hello,")
    string_builder.add("World!")
    assert string_builder.output() == "Hello,World!"
    assert string_builder.size() == 12

# test to check output()
def test_output_method_in_string_builder_class():
    string_builder = StringBuilder()
    string_builder.add("Hello, ")
    string_builder.add("World!")
    assert string_builder.output() == "Hello, World!"

# test to check state after add() and size()
def test_to_check_state_after_add_and_size_method_in_string_builder_class():
    string_builder = StringBuilder()
    string_builder.add("")
    assert string_builder.size() == 0
    assert string_builder.output() == ""

# test to check adding multiple strings
def test_to_add_multiple_strings_in_string_builder_class():
    string_builder = StringBuilder()
    string_builder.add("Hello")
    string_builder.add(", ")
    string_builder.add("World")
    string_builder.add("!")
    assert string_builder.output() == "Hello, World!"
    assert string_builder.size() == 13

# test to check whitespace
def test_to_check_whitespace_in_string_builder_class():
    string_builder = StringBuilder()
    string_builder.add("     ")
    assert string_builder.size() == 5
    assert string_builder.output() == "     "

# test to add special characters or numbers
def test_chars_or_nums_in_string_builder_class():
    string_builder = StringBuilder()
    string_builder.add("one, two, three,")
    string_builder.add(" 4, 5, 6")
    assert string_builder.size() == 24
    assert string_builder.output() == "one, two, three, 4, 5, 6"

# testing a very long string
def test_long_string_in_string_builder_class():
    string_builder = StringBuilder()
    string_builder.add("supercalafragilistic")
    string_builder.add("expialadocious")
    assert string_builder.size() == 34
    assert string_builder.output() == "supercalafragilisticexpialadocious"
