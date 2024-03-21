from gendiff_package.generate_diff import generate_diff
import pytest
import os
from tests.test_file_read import get_expected_result


FIXTURES_DIR = os.path.join('tests', 'fixtures')


def get_file_path(filename):
    return os.path.join(FIXTURES_DIR, filename)


@pytest.mark.parametrize("file1_name, file2_name, result_file_path", [
    ('file1.json', 'file2.json', 'result_generate_diff'),
    ('file1.yaml', 'file2.yaml', 'result_generate_diff'),
    ('file1.yml', 'file2.yml', 'result_generate_diff')
])
def test_generate_diff(file1_name, file2_name, result_file_path):
    file1_path = get_file_path(file1_name)
    file2_path = get_file_path(file2_name)
    expected_result = get_expected_result(f'{result_file_path}.txt')
    actual_result = generate_diff(file1_path, file2_path)
    assert actual_result == expected_result
