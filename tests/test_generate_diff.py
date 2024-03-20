from gendiff_package.generate_diff import generate_diff
import pytest


@pytest.mark.parametrize("file_path_1, file_path_2, result_file_path", [
    ('tests/fixtures/file1.json', 'tests/fixtures/file2.json', 'tests/fixtures/result_generate_diff.txt')
])
def test_generate_diff(file_path_1, file_path_2, result_file_path):
    with open(result_file_path, 'r') as file:
        exp_result = file.read()
    assert generate_diff(file_path_1, file_path_2) == exp_result
