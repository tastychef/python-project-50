install:
	poetry install

gendiff:
	poetry run python3 -m gendiff.scripts.gendiff

build:
	poetry build

lint:
	poetry run flake8 gendiff
	poetry run flake8 tests

test:
	poetry run pytest