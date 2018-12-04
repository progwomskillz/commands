from .command import Command


class WriteToDbCommand(Command):
    def __init__(self, session, object_to_write):
        self.session = session
        self.object_to_write = object_to_write

    def execute(self):
        self.session.add(self.object_to_write)
        return True

    def undo(self):
        self.session.delete(self.object_to_write)
