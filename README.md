# Вычислитель отличий (gendiff)
***
[![Actions Status](https://github.com/Kucher1995/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Kucher1995/python-project-50/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/3f4df24e809347c8ebf7/maintainability)](https://codeclimate.com/github/Kucher1995/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/3f4df24e809347c8ebf7/test_coverage)](https://codeclimate.com/github/Kucher1995/python-project-50/test_coverage)
[![Actions Status](https://github.com/Kucher1995/python-project-50/actions/workflows/my_workflow.yml/badge.svg)](https://github.com/Kucher1995/python-project-50/actions)
***
## Как найти различия между двумя файлами

1. Файлы для соавнения должны находиться в папке tests/fixtures.
2. Выполните в терминале команду:
```
poetry run gendiff tests/fixtures/your_files1.json tests/fixtures/your_file2.json
```
3. Названия your_file1.json и your_file2.json нужно заменить на названия ваших файлов
## Форматы вывода

Для выбора формата вывода различий, укажите флаг -f с названием форматтера. Возможные форматтеры:

- stylish (по умолчанию)
- plain
- json

#### Примеры команд для разных форматов вывода:


1. Вывод в стиле stylish
```
poetry run gendiff tests/fixtures/file1.json tests/fixtures/file2.json
```
```
make diff_yml
```
2. Вывод в формате plain
```
poetry run gendiff -f plain tests/fixtures/file1.json tests/fixtures/file2.json
```
```
make diff_plain
```
3. Вывод в формате json
```
poetry run gendiff -f json tests/fixtures/file1.json tests/fixtures/file2.json
```
```
make diff_json
```
## Пример работы
[![asciicast](https://asciinema.org/a/df1gO3WsOOA4yCcH64bO3pSsO.svg)](https://asciinema.org/a/df1gO3WsOOA4yCcH64bO3pSsO)
***
[![asciicast](https://asciinema.org/a/KTB5VKQ9uZdlmyDLdBO9HLAK7.svg)](https://asciinema.org/a/KTB5VKQ9uZdlmyDLdBO9HLAK7)
***
[![asciicast](https://asciinema.org/a/OHwfMOrBzeuJnMm1cc2N57WD0.svg)](https://asciinema.org/a/OHwfMOrBzeuJnMm1cc2N57WD0)
***
[![asciicast](https://asciinema.org/a/3RaaAr1nOIMdr2aA7NruPwq5M.svg)](https://asciinema.org/a/3RaaAr1nOIMdr2aA7NruPwq5M)
