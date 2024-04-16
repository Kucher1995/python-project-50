import pytest
from gendiff.formatters.stylish import to_str, make_stylish_result
from tests.utils import get_input_data, get_expected_result


@pytest.mark.parametrize('input_value, expected_value', [
    (None, 'null'),
    (True, 'true'),
    ('string', "string"),
    (10, '10'),
    (10.0, '10.0'),
])
def test_to_str(input_value, expected_value):
    assert to_str(input_value) == expected_value


@pytest.fixture
def input_diff():
    return get_input_data('diff.json')


@pytest.fixture
def expected_result():
    return get_expected_result('stylish.txt')


def test_make_stylish_result(input_diff, expected_result):
    assert make_stylish_result(input_diff) == expected_result
