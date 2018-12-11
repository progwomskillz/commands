from commands.command import Command


class WriteToDbCommand(Command):
    def __init__(self, db_service):
        self.db_service = db_service

    def execute(self):
        self.db_service.save()
        return True

    def undo(self):
        self.db_service.delete()
