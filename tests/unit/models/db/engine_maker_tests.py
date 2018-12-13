import unittest

from sqlalchemy.engine import Engine

from models.db.engine_maker import EngineMaker


class EngineMakerTests(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_engine_init(self):
        engine_maker = EngineMaker()
        engine = engine_maker.make_engine()
        self.assertIsInstance(engine, Engine)
