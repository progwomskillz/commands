import os

import requests

from commands.command import Command
from exceptions.env_var_not_set import EnvVarNotSet


class SendEmailCommand(Command):
    def __init__(self, message):
        self.message = message

    def execute(self):
        self.__set_vars_from_env()
        requests.post(self.url, auth=('api', self.token), data=self.message)
        return False

    def __set_vars_from_env(self):
        self.url = self.__get_url_from_env()
        self.token = self.__get_token_from_env()

    def __get_url_from_env(self):
        try:
            return os.environ['EMAIL_URL']
        except KeyError:
            raise EnvVarNotSet('Set the EMAIL_URL environment variable')

    def __get_token_from_env(self):
        try:
            return os.environ['EMAIL_TOKEN']
        except KeyError:
            raise EnvVarNotSet('Set the EMAIL_TOKEN environment variable')
