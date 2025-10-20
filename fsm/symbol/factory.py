from fsm.base import StateMachineFactory as BaseFactory
from .machine import StateMachine
from .input_iterator import InputIterator
from .state import State
from .transition import TransitionActivator


class StateMachineFactory(BaseFactory):
    def __init__(self):
        pass

    def create_state_machine(self):
        return StateMachine()

    def create_state(self):
        return State()

    def create_transition_activator(self, value):
        if type(value) != str or len(value) != 1:
            raise TypeError(
                "Symbol State Machine only accepts characters to activate transitions"
            )
        return TransitionActivator(value)

    def create_input_iterator(self, input_data):
        if type(input_data) != str:
            raise TypeError("Symbol State Machine only accepts strings as input")
        return InputIterator(input_data)
