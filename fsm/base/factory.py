from abc import ABC, abstractmethod


# constructs state machine tools
class StateMachineFactory(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def create_state_machine(self):
        pass

    @abstractmethod
    def create_state(self):
        pass

    @abstractmethod
    def create_transition_activator(self, value):
        pass

    @abstractmethod
    def create_input_iterator(self, input_data):
        pass
