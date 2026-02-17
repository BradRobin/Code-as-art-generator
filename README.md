# Python Code Structure Parser

This project provides a Python-based parser that analyzes Python code snippets and extracts structural elements such as keywords, variables, and indentation into a structured JSON format. This is particularly useful for applications like "Code-as-Art" generators where the visual structure of code is paramount.

## Features

- **Keyword Extraction**: Identifies Python keywords (e.g., `def`, `class`, `if`).
- **Variable Identification**: Distinguishes variables and function names from keywords.
- **Indentation Tracking**: Preserves indentation levels, critical for Python's structure.
- **JSON Output**: Exports the parsed data in a clean, easy-to-consume JSON format.

## Project Structure

```
Code-as-art-generator/
├── src/
│   └── parser.py       # Main parser implementation
├── tests/
│   └── test_parser.py  # Unit tests
└── README.md
```

## Usage

### Basic Example

You can use the `PythonCodeParser` class to parse a string of Python code.

```python
from src.parser import PythonCodeParser

code = """
def greet(name):
    if name:
        print(f"Hello, {name}!")
    else:
        print("Hello, World!")
"""

parser = PythonCodeParser()
json_output = parser.to_json(code)
print(json_output)
```

### JSON Output Format

The output is a list of token objects:

```json
[
  {
    "type": "keyword",
    "value": "def",
    "line": 2,
    "column": 0
  },
  {
    "type": "variable",
    "value": "greet",
    "line": 2,
    "column": 4
  },
  ...
]
```

## Running Tests

To run the unit tests, execute the following command from the project root:

```bash
python -m unittest discover tests
```
