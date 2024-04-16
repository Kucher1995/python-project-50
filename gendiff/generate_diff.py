from gendiff.parser import parser_file
from gendiff.generator import generate
from gendiff.format.__init__ import format_diff


def generate_diff(file1, file2, formatter='stylish'):
    '''Reading files and receiving the scan result in the required format'''
    data1 = parser_file(file1)
    data2 = parser_file(file2)
    diff = generate(data1, data2)
    return format_diff(diff, formatter)
