import configparser
import os


class EnvInterpolation(configparser.BasicInterpolation):
    """Interpolation which expands environment variables in values."""

    def before_get(self, parser, section, option, value, defaults):
        value = super().before_get(parser, section, option, value, defaults)
        return os.path.expandvars(value)

config = configparser.ConfigParser(interpolation=EnvInterpolation())
print(config.read('new_interpolation.ini'))
print(config['section1']['my_dir'])
print(config['section1']['my_path'])