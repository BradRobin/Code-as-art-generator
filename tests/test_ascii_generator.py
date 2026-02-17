
import unittest
import os
import shutil
import sys

# Add src to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from ascii_generator import AsciiArtGenerator

class TestAsciiGenerator(unittest.TestCase):
    def setUp(self):
        self.generator = AsciiArtGenerator()
        self.test_output_dir = "tests/test_outputs"
        if not os.path.exists(self.test_output_dir):
            os.makedirs(self.test_output_dir)

    def tearDown(self):
        if os.path.exists(self.test_output_dir):
            shutil.rmtree(self.test_output_dir)

    def test_mapping_if_statement(self):
        tokens = [
            {'type': 'keyword', 'value': 'if', 'line': 1, 'column': 0},
            {'type': 'variable', 'value': 'x', 'line': 1, 'column': 3},
        ]
        output = self.generator.generate(tokens)
        self.assertIn("<?>", output)

    def test_mapping_function_def(self):
        tokens = [
            {'type': 'keyword', 'value': 'def', 'line': 1, 'column': 0},
            {'type': 'variable', 'value': 'func', 'line': 1, 'column': 4},
        ]
        output = self.generator.generate(tokens)
        self.assertIn("[F]", output)

    def test_indentation_visual(self):
        tokens = [
            {'type': 'keyword', 'value': 'if', 'line': 1, 'column': 0},
            {'type': 'variable', 'value': 'print', 'line': 2, 'column': 4}, # indentation
        ]
        output = self.generator.generate(tokens)
        # Should have indentation pipe
        self.assertIn(" |  ", output)

    def test_file_saving(self):
        content = "test content"
        filename = "test_art.txt"
        filepath = self.generator.save_to_file(content, filename, self.test_output_dir)
        
        self.assertTrue(os.path.exists(filepath))
        with open(filepath, 'r') as f:
            read_content = f.read()
        self.assertEqual(read_content, content)

if __name__ == '__main__':
    unittest.main()
