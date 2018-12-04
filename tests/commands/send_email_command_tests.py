import unittest

from ...commands.send_email_command import SendEmailCommand


class SendEmailCommandTest(unittest.TestCase):
    def setUp(self):
        from_email = 'MailGun User <postmaster@'
        from_email += 'sandbox594416194b3848e79afe9592cc671be9.mailgun.org>'
        message = {
            'from': from_email,
            'to': 'n.skubak@storytelling-software.com',
            'subject': 'MailGun',
            'text': 'Hello',
        }
        self.command = SendEmailCommand(message)

    def test_execute(self):
        self.assertFalse(self.command.execute())


if __name__ == '__main__':
    unittest.main()
