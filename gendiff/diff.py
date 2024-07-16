from typing import Any

from gendiff import consts, parser
from gendiff.format import formatters


def generate_diff(
    file_path_1: str,
    file_path_2: str,
    format: str = consts.STYLISH,
) -> str:
    """
    Generate a textual formatted diff report between two files.

    Args:
        file_path_1: Path to the first file to compare.
        file_path_2: Path to the second file to compare.
        formatter (opt): Function to format the diff output. Default: stylish.
    """
    file_1_data = parser.parse_data_from_file(file_path_1)
    file_2_data = parser.parse_data_from_file(file_path_2)
    diffs = get_diffs(file_1_data, file_2_data)
    formatter = formatters.get_formatter(format)

    return formatter(diffs)


def get_diffs(
    dict_1: dict[str, Any],
    dict_2: dict[str, Any],
) -> list[dict[str, Any]]:
    """
    Creates a list of dictionaries representing the differences
    between two initial dictionaries.

    Returns:
        List contains dictionaries of diff items.
        For nested dictionaries, it contains recursive diff lists.
    """
    keys = sorted(set(dict_1).union(dict_2))
    return [create_diff_item(key, dict_1, dict_2) for key in keys]


def create_diff_item(
    key: str,
    dict_1: dict[str, Any],
    dict_2: dict[str, Any],
) -> dict[str, Any]:
    """
    Generates a dictionary representing of a single diff item.

    Returns:
        Dictionary contains the status of the item, key and values.
    """
    status = calculate_status(key, dict_1, dict_2)

    if status == consts.NESTED:
        return {
            consts.KEY: key,
            consts.STATUS: consts.NESTED,
            consts.ELEMENTS: get_diffs(dict_1.get(key), dict_2.get(key)),
        }

    if status == consts.CHANGED:
        return {
            consts.KEY: key,
            consts.STATUS: status,
            consts.BEFORE: dict_1.get(key),
            consts.AFTER: dict_2.get(key),
        }

    # The only one dict contains the key or both dicts contain the same value
    value = dict_1.get(key) if key in dict_1 else dict_2.get(key)

    return {
        consts.KEY: key,
        consts.STATUS: status,
        consts.VALUE: value,
    }


def calculate_status(
    key: str,
    dict_1: dict[str, Any],
    dict_2: dict[str, Any]
) -> str:
    """
    Determines the status of an item based on its presence and values.
    """
    value_1, value_2 = dict_1.get(key), dict_2.get(key)

    if key not in dict_1:
        return consts.ADDED

    if key not in dict_2:
        return consts.DELETED

    if value_1 == value_2:
        return consts.UNCHANGED

    if is_nested_diff(key, dict_1, dict_2):
        return consts.NESTED

    return consts.CHANGED


def is_nested_diff(
    key: str,
    dict_1: dict[str, Any],
    dict_2: dict[str, Any]
) -> bool:
    return (
        isinstance(dict_1.get(key), dict)
        and isinstance(dict_2.get(key), dict)
    )


def get_status(diff_item: dict[str, Any]) -> str:
    return diff_item[consts.STATUS]


def get_key(diff_item: dict[str, Any]) -> str:
    return diff_item[consts.KEY]


def get_nested_elements(diff_item: dict[str, Any]) -> dict[str, Any]:
    return diff_item[consts.ELEMENTS]


def get_changed_values(diff_item: dict[str, Any]) -> tuple[Any, Any]:
    return diff_item[consts.BEFORE], diff_item[consts.AFTER]


def get_value(diff_item: dict[str, Any]) -> Any:
    return diff_item[consts.VALUE]
