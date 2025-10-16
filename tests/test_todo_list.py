import pytest
from lib.todo_list import TodoList

"""
Given that list is empty
It returns the initial state
"""
def test_todo_list_class_initial_state():
    todo_list = TodoList()
    assert todo_list.incomplete() == []

"""
Given that you add one task,
It returns that task
"""
def test_todo_list_class_to_add_one_task():
    todo_list = TodoList()
    todo_list.add_task("#TODO: Do some learning")
    result = todo_list.incomplete()
    assert result == ["#TODO: Do some learning"]


"""
Given that you add multiple tasks,
It returns them in the list
"""
def test_todo_list_class_to_add_multiple_tasks_at_once():
    todo_list = TodoList()
    todo_list.add_task("#TODO: Do some learning")
    todo_list.add_task("#TODO: Have breakfast")
    todo_list.add_task("#TODO: Do some Exercise")
    result = todo_list.incomplete()
    assert result == ["#TODO: Do some learning", "#TODO: Have breakfast", "#TODO: Do some Exercise"]
    

"""
# Given that you add one task,
# It returns that task is complete()
# """
def test_todo_list_class_to_complete_added_task():
    todo_list = TodoList()
    todo_list.add_task("#TODO: Do some learning")
    todo_list.add_task("#TODO: Do some Exercise")
    todo_list.complete("#TODO: Do some learning")
    result = todo_list.incomplete()
    assert result == ["#TODO: Do some Exercise"]


"""
# Given that you check an unadded task as complete,
# It returns an exception
# """
def test_todo_list_class_with_completing_unadded_task():
    todo_list = TodoList()
    todo_list.add_task("#TODO: Do some learning")
    with pytest.raises(KeyError) as e:
        todo_list.complete("#TODO Walk the dog")
    error_message = str(e.value).strip("'")
    assert error_message == "#TODO Walk the dog not found"


"""
# Given that you add an invalid task,
# It returns an exception
# """
def test_todo_list_class_with_invalid_task_raising_exception():
    todo_list = TodoList()
    with pytest.raises(Exception) as e:
        result = todo_list.add_task("")
    error_message = str(e.value)
    assert error_message == "Invalid input!"