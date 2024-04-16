import pytest
from gendiff.formatters.json import format_diff_json
from tests.utils import get_input_data, get_expected_result


@pytest.fixture
def input_diff():
    return get_input_data('diff.json')


@pytest.fixture
def expected_result():
    return get_expected_result('json.txt')


def test_format_diff_json(input_diff, expected_result):
    assert format_diff_json(input_diff) == expected_result
