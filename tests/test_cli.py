
import unittest
import sys
import os
import subprocess
from io import StringIO

# Add src to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

class TestCLI(unittest.TestCase):
    def test_help_flag(self):
        result = subprocess.run(
            [sys.executable, "codeart.py", "--help"],
            capture_output=True,
            text=True
        )
        self.assertEqual(result.returncode, 0)
        self.assertIn("Code-as-Art Generator", result.stdout)

    def test_ascii_mode(self):
        # Use simple file for input
        input_file = "codeart.py"
        result = subprocess.run(
            [sys.executable, "codeart.py", input_file, "--ascii"],
            capture_output=True,
            text=True
        )
        self.assertEqual(result.returncode, 0)
        # Should output some ascii art
        self.assertIn("[F]", result.stdout) # Function defs likely present in codeart.py

    def test_poetry_mode(self):
        input_file = "codeart.py"
        result = subprocess.run(
            [sys.executable, "codeart.py", input_file, "--poetry"],
            capture_output=True,
            text=True
        )
        self.assertEqual(result.returncode, 0)
        # Should contain some words from strings or comments
        self.assertIn("Code-as-Art Generator", result.stdout) # This string is in codeart.py

    def test_graphics_mode_file_creation(self):
        input_file = "codeart.py"
        output_file = "test_output.png"
        
        # Cleanup before test
        if os.path.exists(output_file):
            os.remove(output_file)
            
        result = subprocess.run(
            [sys.executable, "codeart.py", input_file, "--graphics", "-o", output_file],
            capture_output=True,
            text=True
        )
        self.assertEqual(result.returncode, 0)
        self.assertTrue(os.path.exists(output_file), "Graphics output file should exist")
        
        # Cleanup after test
        if os.path.exists(output_file):
            os.remove(output_file)

if __name__ == "__main__":
    unittest.main()
