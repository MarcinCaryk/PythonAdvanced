import configparser

config = configparser.ConfigParser(interpolation=configparser.BasicInterpolation())
print(config.read('basic_interpolation.ini'))

print('Pictures:', str(config['Paths']['my_pictures']))