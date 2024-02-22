from gendiff.tree import diff
from gendiff.parse_file import open_file


def generate_diff(file_path1, file_path2):
    differences = diff(
        open_file(file_path1),
        open_file(file_path2)
    )
    print(differences)
