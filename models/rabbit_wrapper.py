import json

import pika

from models.environment_settings import EnvironmentSettings
from models.db.user import User
from models.db.engine_maker import EngineMaker
from models.db.session_maker import SessionMaker
from models.services.db_service import DBService
from commands.write_to_db_command import WriteToDbCommand
from models.services.email_service import EmailService
from commands.send_email_command import SendEmailCommand
from models.invoker import Invoker
from exceptions.commands.runtime_error import RuntimeError


class RabbitWrapper(EnvironmentSettings):
    def __init__(self):
        self.host = super()._get_var_from_env('RABBIT_HOST')
        self.queue = super()._get_var_from_env('RABBIT_QUEUE')

        connection_params = pika.ConnectionParameters(host=self.host)
        self.connection = pika.BlockingConnection(connection_params)

        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self.queue)

    def start_consuming(self):
        self.channel.basic_consume(self.__cb, queue=self.queue)
        self.channel.start_consuming()

    def send_message(self, message):
        body = json.dumps(message)
        self.channel.basic_publish(
            exchange='', routing_key=self.queue, body=body
        )
        self.connection.close()

    def __cb(self, ch, method, properties, body):
        user_dict = json.loads(body)
        user = User(**user_dict)

        engine = EngineMaker.make_engine()
        session = SessionMaker.make_session(engine)

        db_service = DBService(session, user)
        write_to_db_command = WriteToDbCommand(db_service)

        email_service = EmailService()
        email_message = {}
        send_email_command = SendEmailCommand(email_service, email_message)

        commands = [write_to_db_command, send_email_command]

        invoker = Invoker(commands)

        try:
            invoker.execute_commands()
            print('Success')
        except RuntimeError:
            print('Error')

        session.close()
        engine.dispose()

        ch.basic_ack(delivery_tag=method.delivery_tag)
