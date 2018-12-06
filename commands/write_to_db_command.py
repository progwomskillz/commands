from commands.command import Command


class WriteToDbCommand(Command):
    def __init__(self, db_service, object_to_db):
        self.db_service = db_service
        self.object_to_db = object_to_db

    def execute(self):
        db_service_result = self.db_service.save(self.object_to_db)
        self.object_from_db = db_service_result
        return True

    def undo(self):
        self.db_service.delete(self.object_from_db)
        return False
