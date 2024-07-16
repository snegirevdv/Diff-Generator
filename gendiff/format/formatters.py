from collections.abc import Callable

from gendiff import consts
from gendiff.format import json_format, plain, stylish

FORMATTERS = {
    consts.STYLISH: stylish.render_view,
    consts.PLAIN: plain.render_view,
    consts.JSON: json_format.render_view,
}


def get_formatter(format: str) -> Callable:
    try:
        return FORMATTERS[format]
    except KeyError as e:
        raise ValueError(consts.FORMATTER_ERROR) from e
