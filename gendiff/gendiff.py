from gendiff.open_file import open_file
from gendiff.gasket import gasket


def generate_diff(file_path1, file_path2, format='stylish'):
    differences = gasket(
        open_file(file_path1),
        open_file(file_path2)
    )

    if format == 'plain':
        return plain(differences)
    elif format == 'json':
        return json_(differences)
    else:
        return stylish(differences)

