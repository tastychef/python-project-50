install:
	poetry install

gendiffchik:
	poetry run python -m gendiff.cli:parser_args -h
	poetry run gendiff -h

build:
	poetry build

lint:
	poetry run flake8 gendiff
	poetry run flake8 tests

test:
	poetry run pytest