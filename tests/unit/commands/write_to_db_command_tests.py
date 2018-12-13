import unittest
from unittest.mock import MagicMock
import os

from commands.write_to_db_command import WriteToDbCommand
from models.services.db_service import DBService
from models.db.session_maker import SessionMaker
from models.db.user import User
from models.db.engine_maker import EngineMaker


class WriteToDbCommandTests(unittest.TestCase):
    def setUp(self):
        os.environ['DB_LOGIN'] = 'test'
        os.environ['DB_PASSWORD'] = 'test'
        os.environ['DB_HOST'] = 'test'
        os.environ['DB_DB'] = 'test'
        engine_maker = EngineMaker()
        engine = engine_maker.make_engine()

        session_maker = SessionMaker()
        session = session_maker.make_session(engine)
        user = User()
        db_service = DBService(session, user)
        db_service.save = MagicMock(return_value=True)
        self.write_to_db_command = WriteToDbCommand(db_service)

    def tearDown(self):
        pass

    def test_execute(self):
        self.assertTrue(self.write_to_db_command.execute())
