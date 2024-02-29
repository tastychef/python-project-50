import json
from pathlib import Path

import yaml


def get_dict_from_file(path_file):
    """Парсит файл и возвращает словарь"""
    file_extension = Path(path_file).suffix
    return open_file(path_file, file_extension)


def open_file(path_file, file_extension):
    if file_extension == '.json':
        return json.load(open(path_file))
    if file_extension in ('.yml', '.yaml'):
        return yaml.safe_load(open(path_file))
