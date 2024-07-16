import argparse

import gendiff


def parse_arguments_from_command() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument(
        "-f",
        "--format",
        metavar="FORMAT",
        choices=[gendiff.STYLISH, gendiff.PLAIN, gendiff.JSON],
        help="set format of output",
        default=gendiff.STYLISH,
    )
    return parser.parse_args()
