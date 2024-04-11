from gendiff.format.stylish import format_diff_stylish
from gendiff.format.plain import format_diff_plain
from gendiff.format.json import format_diff_json


def format_diff(diff, formatter):
    if formatter == 'stylish':
        return format_diff_stylish(diff)
    if formatter == 'plain':
        return format_diff_plain(diff)
    if formatter == 'json':
        return format_diff_json(diff)
    else:
        raise ValueError(f"Unsupported formatter: {formatter}")