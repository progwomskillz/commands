from exceptions.exception_base import ExceptionBase


class RuntimeError(ExceptionBase):
    def __init__(self, text):
        self.message = text
