import unittest
from unittest.mock import MagicMock
import os

from commands.send_email_command import SendEmailCommand
from models.services.email_service import EmailService


class SendEmailCommandTests(unittest.TestCase):
    def setUp(self):
        message = {
            'from': 'Admin <admin@example.com>',
            'to': 'Moder <moder@example.com>',
            'subject': 'New register',
            'message': 'New user registered'
        }
        os.environ['EMAIL_URL'] = 'test'
        os.environ['EMAIL_TOKEN'] = 'test'
        email_service = EmailService(message)
        email_service.send = MagicMock(return_value=True)
        self.send_email_command = SendEmailCommand(email_service)

    def tearDown(self):
        pass

    def test_execute(self):
        self.assertFalse(self.send_email_command.execute())
