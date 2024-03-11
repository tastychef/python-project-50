from gendiff.formaters.stylish import render_stylish
from gendiff.formaters.plain import render_plain
from gendiff.formaters.json import render_json


def get_formatter(formater):
    """Форматирует список отличий в указанном формате. Возвращае строку."""
    if formater == 'stylish':
        return render_stylish
    if formater == 'plain':
        return render_plain
    if formater == 'json':
        return render_json
    raise ValueError(f"Unrecognized formater: {formater}")
