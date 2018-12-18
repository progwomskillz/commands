import unittest
import os

from sqlalchemy.engine import Engine

from models.db.engine_maker import EngineMaker


class EngineMakerTests(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_make_engine(self):
        os.environ['DB_LOGIN'] = 'test'
        os.environ['DB_PASSWORD'] = 'test'
        os.environ['DB_HOST'] = 'test'
        os.environ['DB_DB'] = 'test'
        engine_maker = EngineMaker()
        engine = engine_maker.make_engine()
        self.assertIsInstance(engine, Engine)
