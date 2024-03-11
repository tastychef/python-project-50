# Вычислитель отличий:

[![Actions Status](https://github.com/tastychef/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/tastychef/python-project-50/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/f795081623c9d03c0295/maintainability)](https://codeclimate.com/github/tastychef/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/f795081623c9d03c0295/test_coverage)](https://codeclimate.com/github/tastychef/python-project-50/test_coverage)

# ИНСТРУКЦИИ:

**Вычислитель отличий**

Запускается из командной строки и вычисляет отличия между двумя файлами. На данный момент работает с JSON и YAML.

**Запуск справки:**

`gendiff -h`

**Запуск скрипта c настройками по-умолчанию:**

`gendiff <file_path1> <file_path2>`

**Запуск скрипта с выбором формата вывода:** 

`gendiff --format {stylish, plain, json} <file_path1> <file_path2>`

**Сравнение двух плоских файлов: JSON.**

[![asciicast](https://asciinema.org/a/AeDbt2y6fKW38RnTQPZ6dpbYc.svg)](https://asciinema.org/a/AeDbt2y6fKW38RnTQPZ6dpbYc)

**Сравнение двух плоских файлов: YAML(YML).**

[![asciicast](https://asciinema.org/a/MOBHVcvMI7pCa3hyxIdQhECZM.svg)](https://asciinema.org/a/MOBHVcvMI7pCa3hyxIdQhECZM)

**Сравнение двух файлов c рекурсивной структурой: YAML(YML) или JSON.**

[![asciicast](https://asciinema.org/a/5gOLD7uFqEScvMZBNg3SDKNF3.svg)](https://asciinema.org/a/5gOLD7uFqEScvMZBNg3SDKNF3)

Плоский формат отображения - cравнение двух файлов c рекурсивной структурой YAML(YML) или JSON.

[![asciicast](https://asciinema.org/a/d7YIC5g8pFyvpdiWqm2E1iHTt.svg)](https://asciinema.org/a/d7YIC5g8pFyvpdiWqm2E1iHTt)

Вывод результата сравнения в формате JSON.

[![asciicast](https://asciinema.org/a/jARUTEFXWkUX6Q20UyFUJy6oc.svg)](https://asciinema.org/a/jARUTEFXWkUX6Q20UyFUJy6oc)