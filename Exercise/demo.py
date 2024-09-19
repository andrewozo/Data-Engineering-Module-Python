import configparser

config = configparser.ConfigParser()

config.read('config.ini')

username = config.get('settings', 'username')
password = config.get('settings', 'password')
debug_mode = config.getboolean('settings', 'debug')


print(f'Username: {username}, Password: {password}, Debug Mode: {debug_mode}')

config.set('settings', 'password','new_password1')

with open ('config.ini','w') as configfile:
    config.write(configfile)

