import requests

from models.environment_settings import EnvironmentSettings


class EmailService(EnvironmentSettings):
    def __init__(self):
        self.url = super()._get_var_from_env('EMAIL_URL')
        self.token = super()._get_var_from_env('EMAIL_TOKEN')

    def send(self, message):
        requests.post(self.url, auth=('api', self.token), data=message)
