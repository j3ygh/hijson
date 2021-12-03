basic_values = [
    None,
    True,
    False,
    6,
    -8,
    "",
    "f",
    "oo",
    "\"'\\",
]

empty_list = []
basic_list = basic_values
nested_list = [basic_list]
empty_dict = {}
basic_dict = {str(value): value for value in basic_values}
nested_dict = {"basic_dict": basic_dict}

sample_values = [
    *basic_values,
    empty_list,
    basic_list,
    nested_list,
    empty_dict,
    basic_dict,
    nested_dict,
]

index = [
    "None",
    "True",
    "False",
    "Positive integer",
    "Negative integer",
    "Empty string",
    "Single letter",
    "String",
    "Strange string",
    "Empty list",
    "List",
    "Nested list",
    "Empty dict",
    "Dict",
    "Nested dict",
]
