from commands.command_base import CommandBase


class SendEmailCommand(CommandBase):
    def __init__(self, email_service, message):
        self.email_service = email_service
        self.message = message

    def execute(self):
        self.email_service.send(self.message)
        return False
