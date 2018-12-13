import unittest

from sqlalchemy.orm.session import Session

from models.db.session_maker import SessionMaker


class SessionMakerTests(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_session_init(self):
        mock_engine = True
        session_maker = SessionMaker()
        session = session_maker.make_session(mock_engine)
        self.assertIsInstance(session, Session)
