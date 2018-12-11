import os

from exceptions.environment.cant_be_import import CantBeImport


class EnvironmentSettings:
    def _get_var_from_env(self, key):
        try:
            return os.environ[key]
        except KeyError:
            raise CantBeImport('Set ' + key + ' environment variable')
