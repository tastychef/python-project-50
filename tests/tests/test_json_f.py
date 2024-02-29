import json

from gendiff.tree import diff
from gendiff.formatters.json_f import format_json
from gendiff.parse_file import open_file

def test_json_f():
    result = diff(
        open_file('tests/fixtures/file1.json', json),
        open_file('tests/fixtures/file2.json', json)
    )
    to_json = format_json(result)

    assert json.loads(to_json) == result
