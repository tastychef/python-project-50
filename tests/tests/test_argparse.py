from gendiff.argparse import parser_arg


def test_cli():
    paths = parser_arg(['tests/fixtures/file1.json', 'tests/fixtures/file2.json'])
    assert paths.first_file == 'tests/fixtures/file1.json'
    assert paths.second_file == 'tests/fixtures/file2.json'
    assert paths.format == 'stylish'
