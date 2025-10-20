from abc import ABC, abstractmethod


# iterates over input data to get transition_activators
# example: if a single symbol state machine, the input "hello world"
#          would iterate over symbols in the string ("h" -> "e" -> "l" -> ...)
#          if a word state machine, the input "hi. hello world"
#          would iterate over words in the string ("hi" -> "hello" -> "world")
class InputIterator(ABC):
    @abstractmethod
    def __init__(self, input_data):
        pass

    @abstractmethod
    def __iter__(self):
        pass

    @abstractmethod
    def __next__(self):
        pass
