def json_stringify(value):
    if value is None:
        return "null"
    if value is True:
        return "true"
    if value is False:
        return "false"
    if isinstance(value, int):
        return str(value)
    if isinstance(value, str):
        separator = ''
        children = (
            '\\' + char if char in ['"', "\\"] else char for char in value
        )
        return '"' + separator.join(children) + '"'
    if isinstance(value, list):
        separator = ', '
        children = (json_stringify(child) for child in value)
        return '[' + separator.join(children) + ']'
    if isinstance(value, dict):
        separator = ', '
        children = (
            json_stringify(key) + ': ' + json_stringify(value)
            for key, value in value.items()
        )
        return '{' + separator.join(children) + '}'
