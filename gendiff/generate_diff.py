"""Генерирует различия между файлами."""

from gendiff.formatters.format_diff import format_diff
from gendiff.parse_file import get_dict_from_file
from gendiff.tree import diff


def generate_diff(path_file1, path_file2,
                  format_name='stylish'):
    """Создает различия между двумя файлами
    в выбранном формате и возвращает строку"""
    dict1 = get_dict_from_file(path_file1)
    dict2 = get_dict_from_file(path_file2)
    list_diff = diff(dict1, dict2)
    return format_diff(list_diff, format_name)
