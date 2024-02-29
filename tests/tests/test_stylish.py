from gendiff.parse_file import open_file
from gendiff.tree import diff
from gendiff.formatters.stylish import get_diff_stylish

def test_stylish():
    box_data1 = open_file('tests/fixtures/file1.json', '.json')
    box_data2 = open_file('tests/fixtures/file2.json', '.json')
    box_diff = diff(box_data1, box_data2)
    box_result = open('tests/fixtures/box_stylish.txt').read()


    assert get_diff_stylish(box_diff) == box_result
