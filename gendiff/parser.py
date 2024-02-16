"""Parser module"""

import json
import yaml


def check_format(data, format_name):
    if format_name == '.json':
        return json.load(open(data))
    if format_name in ('.yml', '.yaml'):
        return yaml.safe_load(open(data))

    raise ValueError('Unknown file format')
