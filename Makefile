install:
	poetry install

gendiff:
	poetry gendiff

build:
	poetry build

lint:
	poetry run flake8 gendiff
	poetry run flake8 tests
