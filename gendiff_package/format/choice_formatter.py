from gendiff_package.format.stylish import format_diff_stylish


def format_diff(diff, formatter):
    if formatter == 'stylish':
        return format_diff_stylish(diff)
    else:
        raise ValueError(f"Unsupported formatter: {formatter}")
