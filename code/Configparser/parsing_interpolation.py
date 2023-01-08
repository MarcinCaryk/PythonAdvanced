import configparser

config = configparser.ConfigParser()
print(config.read('config3.ini'))

print('DSN:', str(config['redis']['dsn']))