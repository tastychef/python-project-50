import json

import yaml


def parse(data, format_name):
    """
    The code checks the correctness of the format and,
    depending on the result, translates it into Python,
    and then transposes it into a dictionary
    """
    if format_name == '.json':
        return json.load(open(data))
    if format_name in ('.yml', '.yaml'):
        return yaml.safe_load(open(data))

    raise ValueError('Unknown file format')
