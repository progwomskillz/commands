import unittest
from unittest.mock import MagicMock

from commands.write_to_db_command import WriteToDbCommand
from models.db_service import DBService
from models.user import User


class WriteToDbCommandTest(unittest.TestCase):
    def setUp(self):
        db_service = DBService()
        user = User(first_name='Nik', last_name='S.')
        self.command = WriteToDbCommand(db_service, user)

    def test_execute(self):
        executed = self.command.execute()
        self.assertTrue(executed)

    def test_undo(self):
        self.command.undo()


if __name__ == '__main__':
    unittest.main()
