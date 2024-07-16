# Gendiff: File Comparison Utility

[![Pytest & Flake8](https://github.com/snegirevdv/python-project-50/actions/workflows/check.yml/badge.svg)](https://github.com/snegirevdv/python-project-50/actions/workflows/check.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/8ad89f355494a105cad3/maintainability)](https://codeclimate.com/github/snegirevdv/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/8ad89f355494a105cad3/test_coverage)](https://codeclimate.com/github/snegirevdv/python-project-50/test_coverage)


## Table of contests
- [Features](#features)
- [Minimal Requirements](#minimal-requirements)
- [Installation](#installation)
- [How to Use](#how-to-use)
   - [As a Command-Line Script](#as-a-command-line-script)
   - [As a Library](#as-a-library)
   - [Saving the Diff to a File](#saving-the-diff-to-a-file)
- [Screencasts](#screencasts)

## Features
Gendiff is a command-line script and library for comparing two files and displaying the differences between them.
- **Supported Formats**: Gendiff supports files in JSON and YAML formats.
- **Supported Output Formats**: Gendiff provides three formatters to display differences:
  - **Stylish**: A JSON-like format with changes marked by "+" (added) and "-" (deleted).
  - **Plain**: A plain text report of changes, showing property updates.
  - **JSON**: Standard JSON format representation.
- **Nested Structure Support**: Gendiff handles nested structures, allowing deep comparisons of complex data.

## Minimal Requirements
- Python 3.6 or higher
- Poetry 1.7.1 or higher

## Installation
To install Gendiff, run the following command:
```shell
git clone https://github.com/snegirevdv/python-project-50.git
```
```shell
cd python-project-50
```
```shell
poetry install
```
```shell
poetry build
```
```shell
pip install --user dist/*.whl
```

## How to Use

### As a Command-Line Script:
You can use Gendiff directly from the command line to compare two files.
To get started:
- Install the utility.
- Use the command `gendiff -h` to view the help menu and available options.
- You can choose a formatter by using the `--format` option. Available formatters are `stylish`, `plain`, and `json`. Default value: `stylish`
```shell
gendiff file1.json file2.json
gendiff file1.yml file2.yml --format plain
```

### As a Library:
Gendiff can also be used as a Python library.
```python
from gendiff import generate_diff, get_diffs, PLAIN

# Generate a diff using the default formatter
diff = generate_diff('file1.json', 'file2.json')

# Generate a diff using different formatter (options: STYLISH/PLAIN/JSON)
diff_plain = generate_diff('file1.json', 'file2.json', format=PLAIN)

# Generate a diff as a list of dictionaries
diff = get_diffs('file1.json', 'file2.json')
```

### Saving the Diff to a File:
You can also save the generated diff to a file.
```python
from gendiff import generate_diff, JSON

diff = generate_diff('file1.json', 'file2.json', format=JSON)

with open('diff.json', 'w') as file:
    file.write(diff)
```