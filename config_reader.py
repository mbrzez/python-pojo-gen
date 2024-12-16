import json


def read_config(file_path):
    """
    Reads configuration from a JSON file.

    Args:
        file_path (str): Path to the JSON file.

    Returns:
        dict: Configuration as a dictionary.

    Raises:
        FileNotFoundError: If the file does not exist.
        json.JSONDecodeError: If the file is not valid JSON.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            config = json.load(file)
        return config
    except FileNotFoundError as e:
        raise FileNotFoundError(f'Configuration file not found: {file_path}') from e
    except json.JSONDecodeError as e:
        raise ValueError(f'Invalid JSON format in file: {file_path}') from e
