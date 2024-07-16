import json
from typing import Any

from gendiff.format import consts


def render_view(diffs: list[dict[str, Any]]) -> str:
    """
    Represents the diff as a standard JSON formatted string.
    """
    return json.dumps(diffs, indent=consts.JSON_INDENT)
