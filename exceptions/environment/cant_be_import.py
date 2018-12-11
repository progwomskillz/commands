from exceptions.exception_base import ExceptionBase


class CantBeImport(ExceptionBase):
    def __init__(self, text):
        self.message = text
