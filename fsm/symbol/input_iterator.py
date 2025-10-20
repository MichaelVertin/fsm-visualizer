from fsm.base import InputIterator as BaseInputIterator


class InputIterator(BaseInputIterator):
    def __init__(self, input_data):
        if not isinstance(input_data, str):
            raise TypeError("for symbol iteration, input_data must be of type str")
        self.data = input_data

    def __iter__(self):
        return self

    def __next__(self):
        raise StopIteration
        """
        if self.index < len(self.data):
            item = self.data[self.index]
            self.index += 1
            return item
        else:
            raise StopIteration
        """
