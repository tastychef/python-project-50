import argparse

parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')


def gendiff():
    parser.add_argument(('first_file'))
    parser.add_argument(('second_file'))
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    return args


def main():
    return gendiff()


if __name__ == '__main__':
    main()
