import unittest

from commands.write_to_db_command import WriteToDbCommand
from models.session import Session
from models.user import User


class WriteToDbCommandTest(unittest.TestCase):
    def setUp(self):
        session = Session()
        user = User(first_name='Test', last_name='2')
        self.command = WriteToDbCommand(session, user)

    def test_execute(self):
        self.assertTrue(self.command.execute())

    def test_undo(self):
        self.command.undo()


if __name__ == '__main__':
    unittest.main()
