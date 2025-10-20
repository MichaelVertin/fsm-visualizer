from abc import ABC, abstractmethod


# state in the state machine
class State(ABC):
    def __init__(self):
        self.transitions = dict()

    def add_transition(self, transition_activator, next_state):
        self.transitions[transition_activator] = next_state

    def get_next_state(self, transition_activator):
        return self.transitions.get(transition_activator)
