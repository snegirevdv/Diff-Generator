import os

import pytest

FIXTURES_PATH = "tests/fixtures/"
ANSWERS_PATH = "answers/"


@pytest.fixture
def prepare_data():
    def inner(answer_file_name, formatter, file_path_1, file_path_2):
        answer_path = get_answer_path(answer_file_name, formatter)
        file_path_1 = get_path(file_path_1)
        file_path_2 = get_path(file_path_2)
        answer_path = get_path(answer_path)

        with open(answer_path) as file:
            answer = file.read()

        return answer, file_path_1, file_path_2

    return inner


@pytest.fixture
def update_path():
    def inner(file_path_1, file_path_2):
        file_path_1 = get_path(file_path_1)
        file_path_2 = get_path(file_path_2)
        return file_path_1, file_path_2

    return inner


def get_path(path):
    return os.path.join(FIXTURES_PATH, path)


def get_answer_path(answer_file_name, formatter):
    return f"{ANSWERS_PATH}{formatter}_{answer_file_name}"
