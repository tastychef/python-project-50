#!/usr/bin/env python3
from gendiff.cli import parse_args_cli
from gendiff import generate_diff


def main():
    args = parse_args_cli()
    print(generate_diff(
        args.first_file,
        args.second_file,
        args.format))


if __name__ == '__main__':
    main()
