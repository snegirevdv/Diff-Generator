from typing import Any

from gendiff import consts, diff
from gendiff.format import consts as fconsts


def render_view(diffs: list[dict[str, Any]], prefix: str = "") -> str:
    """
    Represents the diff as a simple text report.
    """
    view = "".join(make_item_block(diff_item, prefix) for diff_item in diffs)

    if not prefix:
        return view.rstrip()

    return view


def make_item_block(diff_item: dict[str, Any], prefix: str) -> str:
    """
    Formats a single diff item into a text line.
    For nested diffs renders an additional view with key prefixes.
    Ignores unchanged items.

    Returns:
        str: A line describing changes and values.
    """
    key = diff.get_key(diff_item)
    status = diff.get_status(diff_item)

    if status == consts.NESTED:
        new_prefix = f"{prefix}{key}{fconsts.DELIMETER}"
        elements = diff.get_nested_elements(diff_item)
        return render_view(elements, new_prefix)

    if status == consts.UNCHANGED:
        return ""

    if status == consts.CHANGED:
        before_value, after_value = diff.get_changed_values(diff_item)
        upd_before_value = stringify_value(before_value)
        upd_after_value = stringify_value(after_value)
        message = get_message(status, upd_before_value, upd_after_value)

    else:
        upd_value = stringify_value(diff.get_value(diff_item))
        message = get_message(status, upd_value)

    return f"{fconsts.PROPERTY} '{prefix}{key}' {message}\n"


def stringify_value(value: Any) -> str:
    """
    Formats the dictionary values in text report format.
    For dictionary values hides the value behind the stub.
    """
    if isinstance(value, dict):
        return fconsts.COMPLEX

    if value is None or isinstance(value, bool):
        return fconsts.VALUE_CONVERTOR[value]

    if isinstance(value, str):
        return f"'{value}'"

    return str(value)


def get_message(status: str, *values) -> str:
    """
    Generates a message describing a diff item.
    """
    return fconsts.MESSAGES[status].format(*values)
