
import os
import sys
from flask import Flask, request, render_template, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename

# Add src to path to import generators
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
from parser import PythonCodeParser
from ascii_generator import AsciiArtGenerator
from visual_generator import VisualArtGenerator
from poetry_generator import PoetryGenerator

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['GENERATED_FOLDER'] = 'static/generated'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max upload

# Ensure directories exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['GENERATED_FOLDER'], exist_ok=True)

ALLOWED_EXTENSIONS = {'py'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '' or not allowed_file(file.filename):
            return redirect(request.url)

        if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            # Process file
            with open(filepath, 'r', encoding='utf-8') as f:
                code_content = f.read()

            parser = PythonCodeParser()
            tokens = parser.parse(code_content)

            # Generate Art
            ascii_gen = AsciiArtGenerator()
            ascii_art = ascii_gen.generate(tokens)

            viz_gen = VisualArtGenerator()
            viz_filename = f"{os.path.splitext(filename)[0]}.png"
            viz_path = os.path.join(app.config['GENERATED_FOLDER'], viz_filename)
            viz_gen.generate(tokens, viz_path)
            
            poetry_gen = PoetryGenerator()
            poem = poetry_gen.generate(tokens)

            return render_template('result.html', 
                                   filename=filename,
                                   code_content=code_content,
                                   ascii_art=ascii_art,
                                   viz_image=viz_filename,
                                   poem=poem)

    return render_template('index.html')

@app.route('/test')
def test():
    return "App is running!"

if __name__ == '__main__':
    app.run(debug=True)
