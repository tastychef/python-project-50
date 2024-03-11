install:
	poetry install

gendiff:
	poetry run gendiff

build:
	poetry build

lint:
	poetry run flake8 gendiff
	poetry run flake8 tests

test:
	poetry run pytest

stylysh:
	poetry run gendiff file1.json file2.json

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml tests/
selfcheck:
	poetry check