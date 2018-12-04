import unittest

from ...models.session import Session
from ...models.user import User


class SessionTest(unittest.TestCase):
    def setUp(self):
        self.user = User(first_name='Test', last_name='1')
        self.session = Session()

    def test_add(self):
        self.session.add(self.user)

    def test_delete(self):
        self.session.delete(self.user)


if __name__ == '__main__':
    unittest.main()
