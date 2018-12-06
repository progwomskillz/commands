import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from exceptions.env_var_not_set import EnvVarNotSet


class DBService:
    def __init__(self):
        self.__set_vars_from_env()

        engine_string = 'postgresql+psycopg2://' + self.db_login + ':'
        engine_string += self.db_password + '@' + self.db_host + '/'
        engine_string += self.db_db
        self.engine = create_engine(engine_string)

        session = sessionmaker(bind=self.engine)
        self.session = session()

    def save(self, object_to_add):
        self.session.add(object_to_add)
        self.session.commit()
        return object_to_add

    def delete(self, object_to_delete):
        self.session.delete(object_to_delete)
        self.session.commit()
        return True

    def close_connection(self):
        self.session.close()
        self.engine.dispose()

    def __set_vars_from_env(self):
        self.db_login = self.__get_db_login_from_env()
        self.db_password = self.__get_db_password_from_env()
        self.db_host = self.__get_db_host_from_env()
        self.db_db = self.__get_db_db_from_env()

    def __get_db_login_from_env(self):
        try:
            return os.environ['DB_LOGIN']
        except KeyError:
            raise EnvVarNotSet('Set DB_LOGIN environment variable')

    def __get_db_password_from_env(self):
        try:
            return os.environ['DB_PASSWORD']
        except KeyError:
            raise EnvVarNotSet('Set DB_PASSWORD environment variable')

    def __get_db_host_from_env(self):
        try:
            return os.environ['DB_HOST']
        except KeyError:
            raise EnvVarNotSet('Set DB_HOST environment variable')

    def __get_db_db_from_env(self):
        try:
            return os.environ['DB_DB']
        except KeyError:
            raise EnvVarNotSet('Set DB_DB environment variable')
