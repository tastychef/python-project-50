install:
	poetry install

gendiff:
	poetry run python -m gendiff.scripts.main -h
	poetry run gendiff -h

build:
	poetry build

lint:
	poetry run flake8 gendiff
	poetry run flake8 tests

test:
	poetry run pytest