import unittest
from unittest.mock import MagicMock

from models.invoker import Invoker
from models.db_service import DBService
from models.user import User
from commands.write_to_db_command import WriteToDbCommand
from models.email_service import EmailService
from commands.send_email_command import SendEmailCommand


class InvokerTest(unittest.TestCase):
    def setUp(self):
        commands = []

        db_service = DBService()
        returned_user = User(id=10, first_name='Nik', last_name='S.')
        db_service.save = MagicMock(return_value=returned_user)
        db_service.delete = MagicMock(return_value=True)
        user = User(first_name='Nik', last_name='S.')
        write_to_db_command = WriteToDbCommand(db_service, user)
        commands.append(write_to_db_command)

        email_service = EmailService()
        email_service.send = MagicMock(return_value=True)
        message = {
            'from': 'Nik <admin@example.com',
            'to': 'user@example.com',
            'subject': 'Test',
            'message': 'Its worked!'
        }
        send_email_command = SendEmailCommand(email_service, message)
        commands.append(send_email_command)

        self.invoker = Invoker(commands)

    def test_execute_commands(self):
        executed = self.invoker.execute_commands()
        self.assertTrue(executed)


if __name__ == '__main__':
    unittest.main()
