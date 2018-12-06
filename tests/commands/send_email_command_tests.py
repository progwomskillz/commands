import unittest
from unittest.mock import MagicMock

from commands.send_email_command import SendEmailCommand
from models.email_service import EmailService


class SendEmailCommandTest(unittest.TestCase):
    def setUp(self):
        email_service = EmailService()
        email_service.send = MagicMock(return_value=True)
        message = {
            'from': 'Nik <admin@example.com',
            'to': 'user@example.com',
            'subject': 'Test',
            'message': 'Its worked!'
        }
        self.command = SendEmailCommand(email_service, message)

    def test_execute(self):
        executed = self.command.execute()
        self.assertFalse(executed)


if __name__ == '__main__':
    unittest.main()
