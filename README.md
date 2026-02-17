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

## ASCII Art Generation

The project includes an `AsciiArtGenerator` that creates abstract visual representations of your code.

### Usage

```python
from src.parser import PythonCodeParser
from src.ascii_generator import AsciiArtGenerator

code = """
def check(x):
    if x > 0:
        return True
    else:
        return False
"""

parser = PythonCodeParser()
tokens = parser.parse(code)

generator = AsciiArtGenerator()
ascii_art = generator.generate(tokens)
print(ascii_art)

# Save to file
generator.save_to_file(ascii_art, "output.txt")
```

### Visual Style

The generator maps keywords to symbols to visualize control flow:

- `[F]`: Function Definition
- `<?>`: Conditional (if)
- ` : `: Else/Alternative
- `(O)`: Loop (for/while)
- `<-`: Return
- `>>>`: Print

**Example Output:**
```
[F]
 |  <?>
 |   |  <-
 |  :
 |   |  <-
```


## Visual Art Generation (Graphics)

Generate abstract visual representations of your code structure using Matplotlib.

### Usage

```python
from src.parser import PythonCodeParser
from src.visual_generator import VisualArtGenerator

code = """
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
"""

parser = PythonCodeParser()
tokens = parser.parse(code)

viz_gen = VisualArtGenerator()
# Save as PNG
viz_gen.generate(tokens, "output.png")
```

The generator maps code elements to colored blocks:
- **Keywords**: Red
- **Variables**: Dark Gray
- **Strings**: Green
- **Numbers**: Blue
- **Operators**: Orange

## Running Tests

To run the unit tests, execute the following command from the project root:


## Automation & Gallery

This repository includes a GitHub Action workflow (`.github/workflows/art-gallery.yml`) that automatically generates art for the source code on every push to the `main` branch.

The generated art is stored in the `gallery/` directory:
- `gallery/ascii/`: ASCII art representations of source files.
- `gallery/graphics/`: Visual (Matplotlib) representations of source files.

To run the gallery generator locally:

```bash
python repo_gallery_gen.py
```

## Web Application

A lightweight Flask web application is included to upload files and view generated art in the browser.

### Local Usage

1.  Install dependencies:
    ```bash
    pip install flask gunicorn
    ```
2.  Run the app:
    ```bash
    python app.py
    ```
3.  Open `http://localhost:5000` in your browser.

### Deployment

The app is ready for deployment on platforms like Heroku.

- **Procfile**: Included for Gunicorn execution.
- **runtime.txt**: Specifies Python version.

To deploy:
1.  Create a Heroku app.
2.  Push command: `git push heroku main`.
