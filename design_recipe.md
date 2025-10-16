# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

>As a user:
estimate_reading_time{
- So that I can manage my time
- I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.
}


>As a user:
- So that I can improve my grammar
- I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

>As a user:
-So that I can keep track of my tasks
-I want a program that I can add todo tasks to and see a list of them.

-So that I can focus on tasks to complete
-I want to mark tasks as complete and have them disappear from the list.



## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
    def estimate_reading_time(text):
"""
    # Parameters: text(string) but will need some int calculation
    maybe calculating time in seconds/min/hour * length of text
    based on the size/length of text.

    Return value: float that returns the estimated time based on the len of text

    Side effects: negative numbers, strings
"""
    pass

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def improve_grammar(text):
"""Corrects a sentence start (with captial letter) 
    and sentence end (with appropriate puncuation mark)
    in a sentence.

    Parameters: (text) - string passed into as a sentence (e.g "hello how are you doing")

    Returns: a boolean reuturn True (if string[0] isupper() and string[-1] in ".?!" 
            else return False ((e.g.["Hello, how are you doing?"]) => True

    Side effects: Value error raised if different datatype is entered other than string
                  Exception error raised if empty string is passed
"""

'"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class TodoList(): # class name
    # public methods
    def __init__(self):
        pass
    # initialised tasks list
    
    def add_task(self, task):
        pass
    # add_task(task: str) -> side effects: stores task as not done

    def complete(self, task):
        pass
    # complete(task: str) -> marks a task complete/doe and it dissapears
    # from incomplete() or raises error if unknown 

    def incomplete(self):
        pass
    # 
    # Edge case: empty input "" returns an exception

# EXAMPLE

def extract_uppercase(mixed_words):
    """Extracts uppercase words from a string

    Parameters: (list all parameters and their types)
        mixed_words: a string containing words (e.g. "hello WORLD")

    Returns: (state the return value and its type)
        a list of strings, each one a word (e.g. ["WORLD"])

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python

"""
Given a text of 200 words,
It returns 1
"""
estimate_reading_time("200 words") => 1

"""
Given a text of 400 words,
It returns 2
"""
estimate_reading_time("400 words") => 2

"""
Given a text of 500 words,
It returns 2.5
"""
estimate_reading_time("500 words") => 2.5

"""
Given an empty string,
It raises an error
"""
estimate_reading_time("") 
=> Raises error: "Empty string cannot be estimated!"


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""
Given an uncapitalised or punctuated string of a single word,
It returns False
"""
improve_grammar("hello") => [False]

"""
Given a string with a punctuation at the end,
It returns True
"""
improve_grammar("how are you?") => [False]

"""
Given a string with capitalised at the start
and punctuation at the end,
It returns True
"""
improve_grammar("Hello world, how are you?") => [True]

"""
Given an incorrect datatype (int) entered,
It returns a TypeError
"""
improve_grammar(123) => throws an error

"""
Given an empty string/value
It returns an Exception error
"""
improve_grammar("") => throws an error

________________________________________________________

"""
Given that list is empty
It returns the initial state
"""
def test_todo_list_class_initial_state():
    todo_list = TodoList()
    todo_list.incomplete() => []

"""
Given that you add one task,
It returns that task
"""
def test_todo_list_class_to_add_one_task():
    todo_list = TodoList()
    todo_list.add_task("#TODO: Do some learning")
    todo_list.incomplete() => ["#TODO: Do some learning"]


"""
Given that you add multiple tasks,
It returns them in the list
"""
def test_todo_list_class_to_add_multiple_tasks_at_once():
    todo_list = TodoList()
    todo_list.add_task("#TODO: Do some learning")
    todo_list.add_task("#TODO: Have breakfast")
    todo_list.add_task("#TODO: Do some Exercise")
    toto_list.incomplete() => ["#TODO: Do some learning", "#TODO: Have breakfast", "#TODO: Do some Exercise"]
    

"""
# Given that you add one task,
# It returns that task is complete()
# """
def test_todo_list_class_to_complete_added_task():
    todo_list = TodoList()
    todo_list.add_task("#TODO: Do some learning")
    todo_list.add_task("#TODO: Do some Exercise")
    todo_list.complete("#TODO: Do some learning")
    todo_list.incomplete() => ["#TODO: Do some Exercise"]


"""
# Given that you check an unadded task as complete,
# It returns an exception
# """
def test_todo_list_class_with_completing_unadded_task():
    todo_list = TodoList()
    todo_list.add_task("#TODO: Do some learning")
    error_message => "#TODO Walk the dog not found"


"""
# Given that you add an invalid task,
# It returns an exception
# """
def test_todo_list_class_with_invalid_task_raising_exception():
    todo_list = TodoList()
    error_message => ["Invalid input!"]




# EXAMPLE

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
extract_uppercase("hello WORLD") => ["WORLD"]

"""
Given two uppercase words
It returns a list with both words
"""
extract_uppercase("HELLO WORLD") => ["HELLO", "WORLD"]

"""
Given two lowercase words
It returns an empty list
"""
extract_uppercase("hello world") => []

"""
Given a lower and a mixed case word
It returns an empty list
"""
extract_uppercase("hello WoRLD") => []

"""
Given a lowercase word and an uppercase word with an exclamation mark
It returns a list with the uppercase word, no exclamation mark
"""
extract_uppercase("hello WORLD!") => ["WORLD"]

"""
Given an empty string
It returns an empty list
"""
extract_uppercase("") => []

"""
Given a None value
It throws an error
"""
extract_uppercase(None) throws an error
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]
```

Ensure all test function names are unique, otherwise pytest will ignore them!
