import unittest
import os

from sqlalchemy.orm.session import Session

from models.db.session_maker import SessionMaker
from models.db.engine_maker import EngineMaker


class SessionMakerTests(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_make_session(self):
        os.environ['DB_LOGIN'] = 'test'
        os.environ['DB_PASSWORD'] = 'test'
        os.environ['DB_HOST'] = 'test'
        os.environ['DB_DB'] = 'test'
        engine_maker = EngineMaker()
        engine = engine_maker.make_engine()

        session_maker = SessionMaker()
        session = session_maker.make_session(engine)
        self.assertIsInstance(session, Session)
