import unittest
from unittest.mock import MagicMock

from commands.send_email_command import SendEmailCommand
from models.services.email_service import EmailService


class SendEmailCommandTests(unittest.TestCase):
    def setUp(self):
        email_service = EmailService()
        email_service.send = MagicMock(return_value=True)
        message = {
            'from': None,
            'to': None,
            'subject': None,
            'message': None
        }
        self.send_email_command = SendEmailCommand(email_service, message)

    def tearDown(self):
        pass

    def test_execute(self):
        self.assertFalse(self.send_email_command.execute())
