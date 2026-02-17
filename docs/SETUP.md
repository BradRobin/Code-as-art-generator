# Developer Setup Guide

Welcome to the `Code-as-art-generator` project! This guide will help you set up your development environment and get started with contributing.

## Prerequisites

- **Python**: Version 3.10 or higher.
- **Pip**: Python package manager.
- **Git**: Version control system.

## Installation

1.  **Clone the Repository**:
    ```bash
    git clone https://github.com/YourUsername/Code-as-art-generator.git
    cd Code-as-art-generator
    ```

2.  **Create a Virtual Environment** (Recommended):
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate
    ```

3.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Project Structure

- `src/`: Core logic (parser, generators).
- `tests/`: Unit tests.
- `templates/`: HTML templates for the web app.
- `static/`: Static assets (CSS, JS, generated images).
- `gallery/`: Generated art samples.

## Running Tests

We use `unittest` for testing. Run the full test suite with:

```bash
python -m unittest discover tests
```

## Running the Web App

Start the Flask development server:

```bash
python app.py
```
Access the app at `http://localhost:5000`.

## Generating Documentation

Update the `README.md` if you add new features. We value clear, concise documentation with examples.

## Contributing

1.  Fork the repository.
2.  Create a feature branch (`git checkout -b feature/amazing-feature`).
3.  Commit your changes (`git commit -m 'Add amazing feature'`).
4.  Push to the branch (`git push origin feature/amazing-feature`).
5.  Open a Pull Request.
