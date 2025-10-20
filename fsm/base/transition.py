from abc import ABC, abstractmethod


# primarily serves as as the key in a transition_map
class TransitionActivator(ABC):
    def __init__(self, value):
        self.value = value

    def __hash__(self):
        return hash(self.value)

    def __eq__(self, other):
        if not isinstance(other, TransitionActivator):
            return NotImplemented
        return self.value == other.value
