import json
import os

import pika

from exceptions.env_var_not_set import EnvVarNotSet
from exceptions.command_runtime_error import CommandRuntimeError
from models.user import User
from models.db_service import DBService
from commands.write_to_db_command import WriteToDbCommand
from models.email_service import EmailService
from commands.send_email_command import SendEmailCommand
from models.invoker import Invoker


class RabbitWrapper:
    def __init__(self):
        self.__set_vars_from_env()

        connection_params = pika.ConnectionParameters(host=self.host)
        self.connection = pika.BlockingConnection(connection_params)

        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self.queue)

    def start_consuming(self):
        self.channel.basic_consume(self.__cb, queue=self.queue, no_ack=True)
        self.channel.start_consuming()

    def send_message(self, message):
        body = json.dumps(message)
        self.channel.basic_publish(exchange='', routing_key=self.queue, body=body)
        self.connection.close()

    def __cb(self, ch, method, properties, body):
        user_dict = json.loads(body)
        user = User(**user_dict)

        commands = []

        db_service = DBService()
        command = WriteToDbCommand(db_service, user)
        commands.append(command)

        email_service = EmailService()
        message = {}
        command = SendEmailCommand(email_service, message)
        commands.append(command)

        invoker = Invoker(commands)
        try:
            invoker.execute_commands()
            print('OK')
        except CommandRuntimeError:
            print('Error')

        db_service.close_connection()

    def __set_vars_from_env(self):
        self.host = self.__get_host_from_env()
        self.queue = self.__get_queue_from_env()

    def __get_host_from_env(self):
        try:
            return os.environ['RABBIT_HOST']
        except KeyError:
            raise EnvVarNotSet('Set RABBIT_HOST environment variable')

    def __get_queue_from_env(self):
        try:
            return os.environ['RABBIT_QUEUE']
        except KeyError:
            raise EnvVarNotSet('Set RABBIT_QUEUE environment variable')
