
install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --force-reinstall dist/*.whl

lint:
	poetry run flake8 gendiff_package
	poetry run flake8 tests

test:
	poetry run pytest

check:
	poetry run flake8 gendiff_package
	poetry run flake8 tests
	poetry run pytest

test-cov:
	poetry run coverage run -m pytest
	poetry run coverage report
