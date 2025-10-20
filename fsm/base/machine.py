from abc import ABC, abstractmethod
import uuid


# stores all states (the transitions are stored in these states)
class StateMachine(ABC):
    def __init__(self):
        self.states = dict()
        self.starting_state = None

    def insert_state(self, state, state_id=None):
        if state_id == None:
            state_id = str(uuid.uuid4())
        state_id = str(state_id)
        self.states[state_id] = state
        if not self.starting_state:
            self.starting_state = state
        return state_id

    def remove_state(self, state_id):
        state = self.states.get(state_id)
        if state:
            del self.states[state_id]
        return state

    def set_start_state(self, state_id):
        starting_state = self.states.get(state_id)
        if starting_state:
            self.starting_state = starting_state
        return self.starting_state

    def set_end_state(self, state_id):
        pass
