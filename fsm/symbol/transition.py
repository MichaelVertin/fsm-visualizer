from fsm.base import TransitionActivator as BaseTransitionActivator


class TransitionActivator(BaseTransitionActivator):
    def __init__(self, value):
        if not isinstance(value, str) or len(value) != 1:
            raise TypeError("Symbol must string of length 1")
        super().__init__(value)
