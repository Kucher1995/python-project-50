from gendiff_package.parser import parser_file
from gendiff_package.generator import generate
from gendiff_package.format.choice_formatter import format_diff


def generate_diff(file_path_1, file_path_2, formatter='stylish'):
    '''Reading files and getting the verification result'''
    data1 = parser_file(file_path_1)
    data2 = parser_file(file_path_2)
    diff = generate(data1, data2)
    return format_diff(diff, formatter)
