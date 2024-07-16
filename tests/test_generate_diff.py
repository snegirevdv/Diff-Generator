import gendiff
import pytest
from gendiff import generate_diff


@pytest.mark.parametrize(
    "formatter",
    [gendiff.STYLISH, gendiff.JSON, gendiff.PLAIN],
)
@pytest.mark.parametrize(
    "answer_file_name, file_path_1, file_path_2",
    [
        [
            "plain_plain.txt",
            "json/plain1.json",
            "json/plain2.json",
        ],
        [
            "empty_empty.txt",
            "json/empty.json",
            "json/empty.json",
        ],
        [
            "plain_empty.txt",
            "json/plain1.json",
            "json/empty.json",
        ],
        [
            "plain_plain.txt",
            "yaml/plain1.yml",
            "yaml/plain2.yml",
        ],
        [
            "empty_empty.txt",
            "yaml/empty.yaml",
            "yaml/empty.yaml",
        ],
        [
            "plain_empty.txt",
            "yaml/plain1.yml",
            "yaml/empty.yaml",
        ],
        [
            "recursive.txt",
            "json/recursive1.json",
            "json/recursive2.json",
        ],
        [
            "recursive.txt",
            "yaml/recursive1.yml",
            "yaml/recursive2.yml",
        ],
    ],
)
def test_generate_diff_success(
    prepare_data,
    formatter,
    answer_file_name,
    file_path_1,
    file_path_2
):
    answer, *file_paths = prepare_data(
        answer_file_name,
        formatter,
        file_path_1,
        file_path_2
    )

    assert gendiff.generate_diff(*file_paths, formatter) == answer


def test_parser_not_found_failure(update_path):
    file_paths = update_path("json/plain1.json", "json/plain.json")

    with pytest.raises(FileNotFoundError):
        gendiff.generate_diff(*file_paths)


def test_parser_extension_failure(update_path):
    file_path_1 = "png/incorrect_format_1.png"
    file_path_2 = "png/incorrect_format_2.png"
    file_paths = update_path(file_path_1, file_path_2)

    with pytest.raises(ValueError) as e:
        gendiff.generate_diff(*file_paths)

    assert str(e.value) == "ERROR: Files have incorrect extension"


@pytest.mark.parametrize(
    "file_path_1, file_path_2",
    [
        ["json/plain1.json", "json/invalid.json"],
        ["json/plain1.json", "json/array.json"],
        ["yaml/plain1.yml", "yaml/invalid.yml"],
    ],
)
def test_parser_encoder_failure(update_path, file_path_1, file_path_2):
    file_paths = update_path(file_path_1, file_path_2)

    with pytest.raises(ValueError) as e:
        generate_diff(*file_paths)

    assert str(e.value) == "ERROR: Files contain invalid data"


def test_get_formatter_failure(update_path):
    file_paths = update_path("json/plain1.json", "json/plain2.json")

    with pytest.raises(ValueError) as e:
        generate_diff(*file_paths, "#AAAAAA")

    assert str(e.value) == "ERROR: Invalid formatter name"
