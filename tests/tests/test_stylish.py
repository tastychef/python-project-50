from gendiff.parse_file import open_file
from gendiff.tree import diff
from gendiff.formatters.stylish import get_diff_stylish

def test_stylish():
    flat_data1 = open_file('tests/fixtures/file1.json', '.json')
    flat_data2 = open_file('tests/fixtures/file2.json', '.json')
    box_diff = diff(flat_data1, flat_data2)
    flat_result = open('tests/fixtures/box_json.txt').read()


    assert get_diff_stylish(box_diff) == flat_result
