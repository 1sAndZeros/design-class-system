from lib.todo_list import *
from lib.todo import *

def test_todo_list_initialised():
    my_list = TodoList()
    assert my_list.todos == []

def test_todo_initialised():
    task1 = Todo('Go Shopping')
    task1.task == 'Go Shopping'
    assert task1.complete == False

def test_mark_complete():
    task1 = Todo('Go Shopping')
    task1.mark_complete()
    assert task1.complete == True