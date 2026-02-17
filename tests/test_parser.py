
import unittest
import json
import sys
import os

# Add src to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from parser import PythonCodeParser

class TestPythonCodeParser(unittest.TestCase):
    def setUp(self):
        self.parser = PythonCodeParser()

    def test_variable_extraction(self):
        code = "x = 10"
        result = self.parser.parse(code)
        
        # Filter for variables
        variables = [t for t in result if t['type'] == 'variable']
        self.assertEqual(len(variables), 1)
        self.assertEqual(variables[0]['value'], 'x')

    def test_keyword_extraction(self):
        code = "def my_func(): pass"
        result = self.parser.parse(code)
        
        keywords = [t for t in result if t['type'] == 'keyword']
        keywords_values = [k['value'] for k in keywords]
        self.assertIn('def', keywords_values)
        self.assertIn('pass', keywords_values)

    def test_indentation(self):
        code = """
if True:
    pass
"""
        result = self.parser.parse(code)
        
        indents = [t for t in result if t['type'] == 'indent']
        self.assertTrue(len(indents) > 0)

    def test_json_output(self):
        code = "y = 20"
        json_str = self.parser.to_json(code)
        data = json.loads(json_str)
        self.assertIsInstance(data, list)
        self.assertEqual(data[0]['type'], 'variable')
        self.assertEqual(data[0]['value'], 'y')

if __name__ == '__main__':
    unittest.main()
