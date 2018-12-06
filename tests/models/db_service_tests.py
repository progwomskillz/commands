import unittest
from unittest.mock import MagicMock

from models.db_service import DBService
from models.user import User


class DBServiceTest(unittest.TestCase):
    def setUp(self):
        self.db_service = DBService()

    def tearDown(self):
        self.db_service.close_connection()

    def test_save(self):
        user = User(first_name='Nik', last_name='S.')
        returned_user = User(id=10, first_name='Nik', last_name='S.')
        self.db_service.save = MagicMock(return_value=returned_user)
        saved_user = self.db_service.save(user)
        self.assertEqual(saved_user.__dict__, returned_user.__dict__)

    def test_delete(self):
        user = User(id=10, first_name='Nik', last_name='S.')
        self.db_service.delete = MagicMock(return_value=True)
        deleted_user = self.db_service.delete(user)
        self.assertTrue(deleted_user)


if __name__ == '__main__':
    unittest.main()
