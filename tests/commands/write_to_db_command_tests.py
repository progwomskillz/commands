import unittest
from unittest.mock import MagicMock

from commands.write_to_db_command import WriteToDbCommand
from models.db_service import DBService
from models.user import User


class WriteToDbCommandTest(unittest.TestCase):
    def setUp(self):
        db_service = DBService()
        returned_user = User(id=10, first_name='Nik', last_name='S.')
        db_service.save = MagicMock(return_value=returned_user)
        db_service.delete = MagicMock(return_value=True)
        user = User(first_name='Nik', last_name='S.')
        self.command = WriteToDbCommand(db_service, user)
        self.command.object_from_db = returned_user

    def test_execute(self):
        executed = self.command.execute()
        self.assertTrue(executed)

    def test_undo(self):
        executed = self.command.undo()
        self.assertFalse(executed)


if __name__ == '__main__':
    unittest.main()
