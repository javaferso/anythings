import configparser

# Crea un objeto ConfigParser
config = configparser.ConfigParser()

# Lee el archivo de configuración
config.read('config.ini')

# Lee un valor del archivo de configuración
api_key = config.get('API', 'key')

# Modifica un valor en el archivo de configuración
config.set('API', 'key', 'new_api_key')

# Guarda los cambios en el archivo de configuración
with open('config.ini', 'w') as configfile:
    config.write(configfile)
