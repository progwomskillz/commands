import unittest

from models.invoker import Invoker
from commands.write_to_db_command import WriteToDbCommand
from models.session import Session
from models.user import User
from commands.send_email_command import SendEmailCommand


class InvokerTest(unittest.TestCase):
    def setUp(self):
        commands = []

        session = Session()
        user = User(first_name='Test', last_name='3')
        write_to_db_command = WriteToDbCommand(session, user)
        commands.append(write_to_db_command)

        from_email = 'MailGun User '
        from_email += '<postmaster@sandbox594416194b3848e79afe9592cc671be9'
        from_email += '.mailgun.org>'
        message = {
            'from': from_email,
            'to': 'n.skubak@storytelling-software.com',
            'subject': 'MailGun',
            'text': 'Hello',
        }
        send_email_command = SendEmailCommand(message)
        commands.append(send_email_command)

        self.invoker = Invoker(commands)

    def test_execute_commands(self):
        self.invoker.execute_commands()

    def test_undo_commands(self):
        self.invoker.undo_commands()


if __name__ == '__main__':
    unittest.main()
