import pytest
from fsm.python_test import PythonTest

def test_initial():
    test_val = "Hello, World!"
    my_obj = PythonTest(val=test_val)
    assert my_obj.get_val() == test_val


