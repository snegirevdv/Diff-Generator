from gendiff import consts

# Common
VALUE_CONVERTOR = {
    True: "true",
    False: "false",
    None: "null",
}

# Stylish
INDENT_SIZE = 4

SPACE = " "
START_LINE = "{\n"
FINISH_LINE = "}\n"

PREFIXES = {
    consts.DELETED: "-",
    consts.UNCHANGED: " ",
    consts.NESTED: " ",
    consts.ADDED: "+",
}

# Plain
PROPERTY = "Property"
COMPLEX = "[complex value]"
DELIMETER = "."

MESSAGES = {
    consts.ADDED: "was added with value: {}",
    consts.DELETED: "was removed",
    consts.CHANGED: "was updated. From {} to {}",
}

# JSON
JSON_INDENT = 3
