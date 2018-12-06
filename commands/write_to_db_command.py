from .command import Command


class WriteToDbCommand(Command):
    def __init__(self, session, object_for_db):
        self.session = session
        self.object_for_db = object_for_db

    def execute(self):
        session_result = self.session.add(self.object_for_db)
        setattr(self, 'object_from_db', session_result)
        return True

    def undo(self):
        self.session.delete(self.object_from_db)
