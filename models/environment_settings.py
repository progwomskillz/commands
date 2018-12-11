import os
from exceptions.env_var_not_set import EnvVarNotSet


class EnvironmentSettings:
    def _get_var_from_env(self, key):
        try:
            return os.environ[key]
        except KeyError:
            raise EnvVarNotSet('Set ' + key + ' environment variable')
