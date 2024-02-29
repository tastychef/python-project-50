from gendiff.formatters.stylish import stylish
from gendiff.formatters.json_f import format_json


def format_diff(list_diff, format_name):
    """Форматирует список различий в указанном формате и возвращает строку"""
    if format_name == 'stylish':
        return stylish(list_diff)
    elif format_name == 'json':
        return format_json(list_diff)
    raise 'Формат не найден!'
