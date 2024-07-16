#!/usr/bin/env python3

import gendiff
from gendiff import cli


def main() -> None:
    args = cli.parse_arguments_from_command()
    print(gendiff.generate_diff(args.first_file, args.second_file, args.format))


if __name__ == "__main__":
    main()
