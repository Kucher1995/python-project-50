from gendiff.parser import get_parse_data_from_file
from gendiff.generator import generate
from gendiff.formatters.choice_formatter import format_diff


def generate_diff(file1, file2, formatter='stylish'):
    '''Reading files and receiving the scan result in the required format'''
    data1 = get_parse_data_from_file(file1)
    data2 = get_parse_data_from_file(file2)
    diff = generate(data1, data2)
    return format_diff(diff, formatter)
