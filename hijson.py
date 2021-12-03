def safe(char):
    escape = "\\"
    escape_needed = {'"', "\\"}
    if char in escape_needed:
        return escape + char
    else:
        return char


def stringify(value):
    if value is None:
        return "null"
    if value is True:
        return "true"
    if value is False:
        return "false"
    if isinstance(value, int):
        return str(value)
    if isinstance(value, str):
        separator = ""
        children = (safe(char) for char in value)
        return '"' + separator.join(children) + '"'
    if isinstance(value, list):
        separator = ", "
        children = (stringify(child) for child in value)
        return "[" + separator.join(children) + "]"
    if isinstance(value, dict):
        separator = ", "
        children = (
            stringify(key) + ": " + stringify(value)
            for key, value in value.items()
        )
        return "{" + separator.join(children) + "}"


def parse(string):
    if string == "null":
        return None
    if string == "true":
        return True
    if string == "false":
        return False
    if string.lstrip("-").isnumeric():
        return int(string)
    if string.startswith('"'):
        value = ""
        escaped = False
        for char in string[1:]:
            if escaped:
                if char in {'"', "\\"}:
                    value += char
                    escaped = False
                else:
                    raise ValueError("Unterminated string.")
            else:
                if char == '"':
                    return value
                if char == "\\":
                    escaped = True
                else:
                    value += char
    if string.startswith("["):
        return []
    if string.startswith("{"):
        return {}


dumps = stringify
loads = parse
