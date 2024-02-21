from gendiff.gasket import gasket
from gendiff.parser import open_file


def generate_diff(file_path1, file_path2):
    differences = gasket(
        open_file(file_path1),
        open_file(file_path2)
    )
    print(differences)
