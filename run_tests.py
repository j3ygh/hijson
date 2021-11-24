import unittest
import json
from parsers import stringify


class JsonStringifyTestCase(unittest.TestCase):
    def test_null(self):
        value = None
        self.assertEqual(stringify(value), json.dumps(value))

    def test_true(self):
        value = True
        self.assertEqual(stringify(value), json.dumps(value))

    def test_false(self):
        value = False
        self.assertEqual(stringify(value), json.dumps(value))

    def test_integer(self):
        value = 6
        self.assertEqual(stringify(value), json.dumps(value))

    def test_negative_integer(self):
        value = -8
        self.assertEqual(stringify(value), json.dumps(value))

    def test_empty_string(self):
        value = ''
        self.assertEqual(stringify(value), json.dumps(value))

    def test_single_letter_string(self):
        value = 'f'
        self.assertEqual(stringify(value), json.dumps(value))

    def test_string(self):
        value = 'oo'
        self.assertEqual(stringify(value), json.dumps(value))

    def test_strange_string(self):
        value = '"\'\\'
        self.assertEqual(stringify(value), json.dumps(value))

    def test_empty_(self):
        value = []
        self.assertEqual(stringify(value), json.dumps(value))

    def test_array(self):
        value = [None, True, False, 6, -8, '', 'f', 'oo']
        self.assertEqual(stringify(value), json.dumps(value))

    def test_empty_object(self):
        value = {}
        self.assertEqual(stringify(value), json.dumps(value))

    def test_object(self):
        value = {
            'None': None,
            'True': True,
            'False': False,
            '': '',
            'f': 'f',
            'oo': 'oo',
        }
        self.assertEqual(stringify(value), json.dumps(value))


if __name__ == "__main__":
    unittest.main()
