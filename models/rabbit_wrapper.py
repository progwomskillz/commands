import json
import os

import pika

from commands.send_email_command import SendEmailCommand
from commands.write_to_db_command import WriteToDbCommand
from exceptions.env_var_not_set import EnvVarNotSet
from models.invoker import Invoker
from models.db_service import Session
from models.user import User


class RabbitWrapper:
    def __init__(self):
        self.__set_vars_from_env()

        connection_params = pika.ConnectionParameters(host=self.host)
        connection = pika.BlockingConnection(connection_params)

        self.channel = connection.channel()
        self.channel.queue_declare(queue=self.queue)

    def start_consuming(self):
        self.channel.basic_consume(self.__cb, queue=self.queue, no_ack=True)
        self.channel.start_consuming()

    def __cb(self, ch, method, properties, body):
        user_dict = json.loads(body)
        user = User(**user_dict)

        commands = []

        session = Session()
        command = WriteToDbCommand(session, user)
        commands.append(command)

        command = SendEmailCommand({})
        commands.append(command)

        invoker = Invoker(commands)
        try:
            invoker.execute_commands()
            print('OK')
        except Exception as e:
            print(e)
            invoker.undo_commands()

        session.close_connection()

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
