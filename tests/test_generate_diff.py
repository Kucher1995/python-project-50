import pytest
import os
from gendiff.generate_diff import generate_diff
from tests.utils import get_expected_result


FIXTURES_DIR = os.path.join('tests', 'fixtures')


def get_file_path(filename):
    return os.path.join(FIXTURES_DIR, filename)


@pytest.mark.parametrize('file1_name, file2_name, formatter', [
    ('file1.1.json', 'file2.1.json', 'stylish'),
    ('file1.1.yml', 'file2.1.yml', 'stylish'),
    ('file1.1.json', 'file2.1.json', 'plain'),
    ('file1.1.yml', 'file2.1.yml', 'plain'),
    ('file1.1.json', 'file2.1.json', 'json'),
    ('file1.1.yml', 'file2.1.yml', 'json')
])
def test_generate_diff(file1_name, file2_name, formatter):
    file1_path = get_file_path(file1_name)
    file2_path = get_file_path(file2_name)
    expected_result = get_expected_result(f'{formatter}.txt')

    actual_result = generate_diff(file1_path, file2_path, formatter)

    assert actual_result == expected_result


@pytest.mark.parametrize('file1_name, file2_name, formatter', [
    ('file1.1.json', 'file3.txt', 'stylish')
])
def test_unsupported_formatter(file1_name, file2_name, formatter):
    file1_path = get_file_path(file1_name)
    file2_path = get_file_path(file2_name)
    with pytest.raises(ValueError):
        generate_diff(file1_path, file2_path, formatter)
