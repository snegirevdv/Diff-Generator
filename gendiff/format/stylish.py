from typing import Any

from gendiff import consts, diff
from gendiff.format import consts as fconsts


def render_view(diffs: list[dict[str, Any]], step: int = 0) -> str:
    """
    Represents the diffs as a stylish, JSON-like fomatted report.
    """
    view = fconsts.START_LINE
    view += "".join(make_item_block(diff_item, step) for diff_item in diffs)
    view += make_indent(step) + fconsts.FINISH_LINE

    if not step:
        return view.rstrip()  # Remove finish \n for main view

    return view


def make_item_block(diff_item: dict[str, Any], step: int) -> str:
    """
    Formats a single diff item into a stylish view block.
    For nested diffs recursivly renders an additional view.

    Returns:
        str: One or two (for changed diffs) lines describing changes and values.

    """
    key = diff.get_key(diff_item)
    status = diff.get_status(diff_item)

    if status == consts.NESTED:
        elements = diff.get_nested_elements(diff_item)
        return (
            make_key_part(key, step, status)
            + render_view(elements, step + 1)
        )

    if status == consts.CHANGED:
        before_value, after_value = diff.get_changed_values(diff_item)
        first_line = (make_key_part(key, step, status=consts.DELETED)
                      + make_value_part(before_value, step))
        second_line = (make_key_part(key, step, status=consts.ADDED)
                       + make_value_part(after_value, step))
        return first_line + second_line

    value = diff.get_value(diff_item)
    return make_key_part(key, step, status) + make_value_part(value, step)


def make_key_part(key: str, step: int, status: str) -> str:
    """
    Makes the left part of the block contain the indent, the prefix, and the key

    Returns:
        str: the intent, the prefix if it needs (+/-) and the key.
    """
    return f"{make_indent(step)}{make_prefix(status)}{key}: "


def make_value_part(value: Any, step: int) -> str:
    """
    Makes the right part of the block contain the value of the item.

    Returns:
        str: JSON-like view of the value.
    """
    if isinstance(value, dict):
        return stringify_dict_value(value, step + 1)
    return stringify_value(value) + "\n"


def stringify_dict_value(subdict: dict[str, Any], step) -> str:
    """
    Formats the dictionary values in JSON-like format.
    """
    view = fconsts.START_LINE

    for key in subdict:
        value = subdict.get(key)
        view += (
            make_key_part(key, step, status=consts.UNCHANGED)
            + make_value_part(value, step)
        )

    view += make_indent(step) + fconsts.FINISH_LINE

    return view


def stringify_value(value: Any) -> str:
    """
    Formats the regular values in JSON-like format.
    """
    if value is None or isinstance(value, bool):
        return fconsts.VALUE_CONVERTOR[value]
    return str(value)


def make_indent(step: int) -> str:
    return fconsts.SPACE * fconsts.INDENT_SIZE * step


def make_prefix(status: str) -> str:
    return fconsts.SPACE * 2 + fconsts.PREFIXES[status] + fconsts.SPACE
