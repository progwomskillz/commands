from exceptions.exception_base import ExceptionBase


class CantBeUndone(ExceptionBase):
    def __init__(self, text):
        self.message = text
