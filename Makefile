install: # Install project
	poetry install

update: # Update dependencies
	poetry update

build: # Build project
	poetry build

lint: # Run flake8
	poetry run flake8

test: # Run pytest
	poetry run pytest

coverage: # Run coverage
	poetry run coverage run -m pytest
	poetry run coverage xml
	poetry run coverage report
