import os

from exceptions.env_var_not_set import EnvVarNotSet


class EmailService:
    def __init__(self):
        self.__set_vars_from_env()

    def __set_vars_from_env(self):
        self.url = self.__get_url_from_env()
        self.token = self.__get_token_from_env()

    def __get_url_from_env(self):
        try:
            return os.environ['EMAIL_URL']
        except KeyError:
            raise EnvVarNotSet('Set EMAIL_URL environment variable')

    def __get_token_from_env(self):
        try:
            return os.environ['EMAIL_TOKEN']
        except KeyError:
            raise EnvVarNotSet('Set EMAIL_TOKEN environment variable')
