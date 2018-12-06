import unittest
from unittest.mock import MagicMock

from models.email_service import EmailService


class EmailServiceTest(unittest.TestCase):
    def setUp(self):
        self.email_service = EmailService()

    def test_send(self):
        self.email_service.send = MagicMock(return_value=True)
        message = {
            'from': 'Nik <admin@example.com',
            'to': 'user@example.com',
            'subject': 'Test',
            'message': 'Its worked!'
        }
        send = self.email_service.send(message)
        self.assertTrue(send)


if __name__ == '__main__':
    unittest.main()
