from gendiff.cli import parsing_args
from gendiff.gendiff import generate_diff


def main():
    """
    основная функция, которая прогоняет
    анализируемые данные через argpars
    и def генератор отличий
    Returns:

    """
    first_file, second_file = parsing_args()
    print(generate_diff(first_file, second_file))


if __name__ == '__main__':
    main()
