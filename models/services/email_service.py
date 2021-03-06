import requests

from models.environment_settings import EnvironmentSettings


class EmailService(EnvironmentSettings):
    def __init__(self, message):
        self.url = super()._get_var_from_env('EMAIL_URL')
        self.token = super()._get_var_from_env('EMAIL_TOKEN')
        self.message = message

    def send(self):
        requests.post(self.url, auth=('api', self.token), data=self.message)
