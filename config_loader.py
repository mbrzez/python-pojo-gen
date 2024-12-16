from config_reader import read_config

config = dict()

try:
    filepath = 'resources/app-config.json'
    config = read_config(filepath)
except (FileNotFoundError, ValueError) as e:
    print(f'Warning: Configuration could not be loaded. {e}')