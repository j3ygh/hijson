import json
from timeit import timeit

from json_parsers import stringify


def get_main(stringify_func, value):
    def main():
        string = stringify_func(value)
        return string

    return main


values = [
    None,
    True,
    False,
    6,
    -8,
    "",
    "f",
    "oo",
    "\"'\\",
    [],
    [None, True, False, 6, -8, "", "f", "oo"],
    [
        None,
        True,
        False,
        6,
        -8,
        "",
        "f",
        "oo",
        [None, True, False, 6, -8, "", "f", "oo"],
    ],
    {},
    {
        "None": None,
        "True": True,
        "False": False,
        "": "",
        "f": "f",
        "oo": "oo",
        "array": [None, True, False, 6, -8, "", "f", "oo"],
    },
    {
        "None": None,
        "True": True,
        "False": False,
        "": "",
        "f": "f",
        "oo": "oo",
        "array": [None, True, False, 6, -8, "", "f", "oo"],
        "object": {
            "None": None,
            "True": True,
            "False": False,
            "": "",
            "f": "f",
            "oo": "oo",
            "array": [None, True, False, 6, -8, "", "f", "oo"],
        },
    },
]
for value in values:
    t1 = timeit(get_main(stringify_func=stringify, value=value))
    t2 = timeit(get_main(stringify_func=json.dumps, value=value))
    result = "Win" if t1 < t2 else "Lose"
    print(result, round(t1, 6), round(t2, 6))
