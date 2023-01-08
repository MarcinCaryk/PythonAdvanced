import configparser

config = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation())
print(config.read('extended_interpolation.ini'))

print('Python dir:', str(config['Marcin']['python_dir']))