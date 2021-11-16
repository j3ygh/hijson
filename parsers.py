import unittest


def json_parse(string):
    if string == "null":
        return None
    if string == "true":
        return True
    if string == "false":
        return False
    if string.lstrip("-").isnumeric():
        return int(string)
    if string.startswith('"') and string.endswith('"'):
        return string.strip('"')
    if string.startswith("[") and string.endswith("]"):
        inside = string[1:-1]
        if inside == "":
            return []
        strings = inside.split(",")
        return [json_parse(string.strip()) for string in strings]
    if string.startswith("{") and string.endswith("}"):
        inside = string[1:-1]
        if inside == "":
            return {}
        pairs = (string.split(":") for string in inside.split(","))
        return {
            json_parse(key.strip()): json_parse(value.strip()) for key, value in pairs
        }


class JSONParseTestCase(unittest.TestCase):
    def test_null(self):
        self.assertEqual(json_parse("null"), None)

    def test_true(self):
        self.assertEqual(json_parse("true"), True)

    def test_false(self):
        self.assertEqual(json_parse("false"), False)

    def test_integer(self):
        self.assertEqual(json_parse("6"), 6)

    def test_negative_integer(self):
        self.assertEqual(json_parse("-8"), -8)

    def test_negative_integer(self):
        self.assertEqual(json_parse('"foo"'), "foo")

    def test_string(self):
        self.assertEqual(json_parse('"foo"'), "foo")

    def test_empty_array(self):
        self.assertEqual(json_parse("[]"), [])

    def test_array(self):
        self.assertEqual(
            json_parse('[null, true, false, 1996, "", "bar"]'),
            [None, True, False, 1996, "", "bar"],
        )

    def test_empty_object(self):
        self.assertEqual(json_parse("{}"), {})

    def test_object(self):
        self.assertEqual(
            json_parse('{"age": 28, "name": "Jimmy Lin"}'),
            {"age": 28, "name": "Jimmy Lin"},
        )

    # def test_nested(self):
    #     self.assertEqual(
    #         json_parse('{"name": "Jimmy Lin", "languages": ["English", "Chinese"]}'),
    #         {"name": "Jimmy Lin", "languages": ["English", "Chinese"]},
    #     )


if __name__ == "__main__":
    unittest.main()
