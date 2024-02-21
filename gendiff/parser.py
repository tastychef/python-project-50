import json

import yaml


def parse(data, type_format):
    if type_format == 'json':
        return json.loads(data)
    elif type_format == 'yaml':
        return yaml.safe_load(data)
    else:
        raise ValueError("gasket")


def open_file(file):
    if str(file).endswith('json'):
        type_format = 'json'
    elif str(file).endswith('yml') or str(file).endswith('yaml'):
        type_format = 'yaml'
    else:
        type_format = 'other'
    data = open(file).read()
    return parse(data, type_format)
