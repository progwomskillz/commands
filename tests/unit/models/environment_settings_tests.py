import unittest
import os

from models.environment_settings import EnvironmentSettings
from exceptions.environment.cant_be_import import CantBeImport


class EnvironmentSettingsTests(unittest.TestCase):
    def setUp(self):
        self.environment_settings = EnvironmentSettings()
        self.key, self.value = 'TEST_VARIABLE', 'TEST_STRING'

    def tearDown(self):
        pass

    def test_get_available_var(self):
        os.environ[self.key] = self.value
        value = self.environment_settings._get_var_from_env(self.key)
        self.assertEqual(value, self.value)
        os.environ.pop(self.key)

    def test_get_unavailable_var(self):
        with self.assertRaises(CantBeImport):
            self.environment_settings._get_var_from_env(self.key)
