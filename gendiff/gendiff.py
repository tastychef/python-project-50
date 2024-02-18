from gendiff.parser import parse
from gendiff.tree import make_tree


def generate_diff(file_path1: str, file_path2: str):
    dict_1 = dict(parse(file_path1))
    dict_2 = dict(parse(file_path2))
    diff = make_tree(dict_1, dict_2)

    return diff
